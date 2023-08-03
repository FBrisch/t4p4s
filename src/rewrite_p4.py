
from hlir16 import hlir


def expr_to_string(expr):
    if expr.node_type == 'Constant':
        if expr.base == 10:
            return f'{expr.value}'
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
    breakpoint()
    print('TODO_COMP')

def printHLIR(hlir):

    import_files = {
        'V1Switch': 'v1model.p4',
        'PSA': 'psa.p4',
    }
    def type_to_str(node):
        if node.node_type == 'Type_Bits':
            return f'bit<{node.size}>'
        return 'TODO_TYPE'

    print(f'#include <{import_files[hlir.news.model]}>')
    print()

    for hdr in hlir.headers.filter(lambda hdr: hdr.name != 'all_metadatas_t'):
        print(f'header {hdr.name} {{')
        for fld in hdr.fields:
            print(f'    {type_to_str(fld.type)} {fld.name};')
        print(f'}}')
        print()

    print(f'struct headers {{')
    for hdrinst in hlir.header_instances.filter(lambda hdrinst: hdrinst.name != 'all_metadatas'):
        print(f'    {hdrinst.urtype.name} {hdrinst.name};')
    print(f'}}')
    print()

    print(f'struct metadata {{')
    for meta in hlir.header_instances['all_metadatas']:
        print(f'    TODO_META {meta.name};')
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
                    print(f'        {stateComponent.call}(')
                    for argument in stateComponent.methodCall.arguments:
                        print(f'          {argument.expression.expr.path.name}.{argument.expression.hdr_ref.name}(')
                    print(f'        );')
                else:
                    print()
                    #normal call/assignment
                        
            if state.selectExpression.node_type == "PathExpression":
                print(f'        transition {state.selectExpression.path.name}')
            else:
                print(f'        transition select({parserHeaderName}.{state.selectExpression.select.components[0].fld_ref.name}.{state.selectExpression.select.components[0].fld_ref.name}){"{"}')
                for case in state.selectExpression.selectCases:
                    if(case.keyset.node_type == 'DefaultExpression'):
                        print(f'          default:')
                    else:
                        print(f'          {case.keyset.value}:{case.state.path.name}')
                if state.selectExpression.select.components[0].fld_ref.name == 'accept':
                    print(f'        transition accept;')
            print(f'    }}')
        print(f'}}')
        print()

    for ctl in hlir.controls:
        params = ', '.join(f'{param.direction} {param.urtype.name} {param.name}' for param in ctl.type.applyParams.parameters)

        print(f'control {ctl.type.name}({params}) {{')

        for action in ctl.actions:
            # TODO
            params = ''
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
        

