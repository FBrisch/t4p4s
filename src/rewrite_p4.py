
from hlir16 import hlir


def expr_to_string(expr):
    if expr.node_type == 'Constant':
        if expr.base == 10:
            return f'{expr.value}'
        if expr.base == 16:
            return f'{expr.value:#X}'
        breakpoint()
        return 'TODO_CONST_EXPR'

    if expr.node_type == 'Member':
        return f'{expr_to_string(expr.expr)}.{expr.member}'

    if expr.node_type == 'MethodCallExpression':
        args = ', '.join(expr_to_string(arg) for arg in expr.arguments)
        if 'path' not in expr.method:
            args = ', '.join(arg for arg in expr.arguments)
            return f'{expr_to_string(expr.method.expr)}.{expr.method.member}({args})'
        return f'{expr.method.path.name}({args})'

    if expr.node_type == 'PathExpression':
        return f'{expr.path.name}'

    if expr.node_type == 'StructExpression':
        args = ', '.join(expr.components.map('expression').map(expr_to_string))
        return f'{{{args}}}'

    if expr.node_type == 'TypeNameExpression':
        return f'{expr.urtype.name}'
    
    if expr.node_type == 'Add':
        return f'{expr_to_string(expr.left)} + {expr_to_string(expr.right)}'
    
    if expr.node_type == 'BAnd':
        return f'{expr_to_string(expr.left)} & {expr_to_string(expr.right)}'
    if expr.node_type == 'LAnd':
        return f'{expr_to_string(expr.left)} && {expr_to_string(expr.right)}'
    if expr.node_type == 'Equ':
        return f'{expr_to_string(expr.left)} == {expr_to_string(expr.right)}'
    if expr.node_type == 'Neq':
        return f'{expr_to_string(expr.left)} != {expr_to_string(expr.right)}'
    if expr.node_type == 'BoolLiteral':
        if expr.value:
            return f'true'
        else:
            return f'false'
    if expr.node_type == 'Declaration_Variable':
        return f' {expr_to_string(expr.type)} {expr.name}'
    if expr.node_type == 'Type_Bits':
        return f' bit<{expr.size}>'
    if expr.node_type == 'Type_Boolean':
        return f' bool'
    if expr.node_type == "StructField":
        return f' {expr_to_string(expr.type)} {expr.name}'
    if expr.node_type == "Type_Name":
        return f' '
    breakpoint()
    return 'TODO_EXPR'

def print_body_component(level, node):
    indent = '    '*level
    
    if node.node_type == 'MethodCallStatement':
        mc = node.methodCall
        exprs = ', '.join(mc.arguments.map('expression').map(expr_to_string))
        
        if 'path' not in mc.method:
            
            name = mc.method.member
            if name == 'emit':
                print(f'{indent}{mc.method.expr.decl_ref.name}.{name}({exprs});')
            elif name == 'apply':
                print(f'{indent}{mc.method.expr.path.name}.{name}({exprs});')
            else:
                print(f'{indent}{mc.type.name}.{name}({exprs});')
            return
        else:
            name = mc.method.path.name
            print(f'{indent}{name}({exprs});')
            return
    if node.node_type == 'AssignmentStatement':
        print(f'{indent}{expr_to_string(node.left)} = {expr_to_string(node.right)};')
        return
    if node.node_type == 'IfStatement':
        print(f'{indent}if({expr_to_string(node.condition)}){{')
        print_body_component(level+1,node.ifTrue)
        print(f'{indent}}}')
        if 'ifFalse' in node:
            print(f'{indent}else{{')
            print_body_component(level+1,node.ifFalse)
            print(f'{indent}}}')
        return
    if node.node_type == 'BlockStatement':
        for component in node.components:
            print_body_component(level,component)
        return
    breakpoint()
    print('TODO_COMP')

def printHLIR(hlir):

    import_files = {
        'V1Switch': 'v1model.p4',
        'PSA': 'psa.p4',
    }

    print(f'#include <{import_files[hlir.news.model]}>')
    print()

    for hdr in hlir.headers:
        if hdr.name == "all_metadatas_t":
            print(f'struct metadata {{')
            for fld in hdr.fields:
                print(f'    {expr_to_string(fld.type)};')
        else:
            print(f'header {hdr.name} {{')
            for fld in hdr.fields:
                print(f'    {expr_to_string(fld)};')
        print(f'}}')
        print()

    print(f'struct headers {{')
    for hdrinst in hlir.header_instances.filter(lambda hdrinst: hdrinst.name != 'all_metadatas_t'):
        print(f'    {hdrinst.urtype.name} {hdrinst.name};')
    print(f'}}')
    print()


    for parser in hlir.parsers:
        params = ', '.join(f'{param.direction} {param.urtype.name} {param.name}' for param in parser.type.applyParams.parameters)
        # breakpoint()
        parserHeaderName = parser.type.applyParams.parameters[1].name
        
        print(f'parser {parser.type.name}({params}) {{')
        for state in parser.states:
            if state.name in ('accept', 'reject'):
                continue

            print(f'    state {state.name} {{')
            for stateComponent in state.components:
                if stateComponent.call == 'extract_header':
                    print(f'        packet.extract(')
                    for argument in stateComponent.methodCall.arguments:
                        print(f'          {argument.expression.expr.path.name}.{argument.expression.hdr_ref.name}')
                    print(f'        );')
                else:
                    print()
                    #normal call/assignment
                        
            if state.selectExpression.node_type == "PathExpression":
                print(f'        transition {state.selectExpression.path.name};')
            else:
                print(f'        transition select({parserHeaderName}.{state.selectExpression.select.components[0].expr.member}.{state.selectExpression.select.components[0].fld_ref.name}){"{"}')
                for case in state.selectExpression.selectCases:
                    if(case.keyset.node_type == 'DefaultExpression'):
                        print(f'          default:{case.state.path.name};')
                    else:
                        print(f'          {case.keyset.value}:{case.state.path.name};')
                if state.selectExpression.select.components[0].fld_ref.name == 'accept':
                    print(f'        transition accept;')
                print('        }')
            print(f'    }}')
        print(f'}}')
        print()

    for ctl in hlir.controls:
        params = ', '.join(f'{param.direction} {param.urtype.name} {param.name}' for param in ctl.type.applyParams.parameters)

        print(f'control {ctl.type.name}({params}) {{')

        for variable in ctl.controlLocals:
            if variable.node_type == "Declaration_Variable":
                print(f'        {expr_to_string(variable)};')

        for action in ctl.actions:
            # TODO
            params = ', '.join(f'{expr_to_string(param.type)} {param.name}' for param in action.parameters.parameters.vec)
        
            print(f'    action {action.name}({params}) {{')
            for comp in action.body.components:
                print_body_component(2, comp)
            print(f'    }}')

        for table in ctl.tables:
            print(f'    table {table.name} {{')

            print(f'        key = {{')
            for keyelem in table.key.keyElements:
                print(f'            {expr_to_string(keyelem.expression)}: {keyelem.matchType.path.name};')
            print(f'        }}')

            print(f'        actions = {{')
            for name in table.actions.map('expression.method.path.name'):
                print(f'            {name};')
            print(f'        }}')

            if 'size' in table:
                print(f'        size = {expr_to_string(table.size.expression)};')

            if 'default_action' in table:
                print(f'        default_action = {expr_to_string(table.default_action.expression)};')

            print(f'    }}')

        print(f'    apply {{')
        for comp in ctl.body.components:
            print_body_component(2, comp)
        print(f'    }}')

        print(f'}}')
        print()
        

