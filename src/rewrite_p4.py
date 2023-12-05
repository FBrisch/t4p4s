
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
        if "action_ref" in expr.method:
            return f'{expr.method.action_ref.name}({args})'
        else:
            return f'{expr.method.path.name}({args})'

    if expr.node_type == 'PathExpression':
        if "table_ref" in expr:
            return f'{expr.table_ref.name}'
        if "action_ref" in expr:
            return f'{expr.action_ref.name}'
        else:
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
        return f' {expr.type_ref.name}'
    if expr.node_type == "LOr":
        return f'{expr_to_string(expr.left)} || {expr_to_string(expr.right)}'
    if expr.node_type == "Parameter":
        return f'{expr_to_string(expr.type)}'
    if expr.node_type == "Type_Specialized":
        return f'{expr.baseType.path.name}'
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
                return f'{indent}{mc.method.expr.decl_ref.name}.{name}({exprs});\r\n'
            elif name == 'apply':
                return f'{indent}{mc.method.expr.table_ref.name}.{name}({exprs});\r\n'
            elif name=='setValid':
                return f'{indent}hdr.{mc.method.expr.member}.{name}({exprs});\r\n'
            elif name=='setInvalid':
                return f'{indent}hdr.{mc.method.expr.member}.{name}({exprs});\r\n'
            elif name=='execute_meter':
                return f'{indent}{mc.method.expr.path.name}.{name}({exprs});\r\n'
            else:
                return f'{indent}{mc.type.name}.{name}({exprs});\r\n'
            return
        else:
            name = mc.method.path.name
            return f'{indent}{name}({exprs});\r\n'
            
    if node.node_type == 'AssignmentStatement':
        return f'{indent}{expr_to_string(node.left)} = {expr_to_string(node.right)};\r\n'
        
    if node.node_type == 'IfStatement':
        statement = ""
        statement += f'{indent}if({expr_to_string(node.condition)}){{\r\n'
        statement += print_body_component(level+1,node.ifTrue)
        statement +=f'{indent}}}\r\n'
        if 'ifFalse' in node:
            statement += f'{indent}else{{\r\n'
            statement += print_body_component(level+1,node.ifFalse)
            statement += f'{indent}}}\r\n'
        return statement
    if node.node_type == 'BlockStatement':
        statement = ""
        for component in node.components:
            statement += print_body_component(level,component)
        return statement
    if node.node_type == 'EmptyStatement':
        return "    "
    breakpoint()
    return 'TODO_COMP'

def printHLIR(hlir):
    returnString = ""
    
    import_files = {
        'V1Switch': 'v1model.p4',
        'PSA': 'psa.p4',
    }

    returnString += f'#include <{import_files[hlir.news.model]}>\r\n'
    print()

    for hdr in hlir.headers:
        if hdr.name == "all_metadatas_t":
            returnString += f'struct metadata {{\r\n'
            for fld in hdr.fields:
                returnString += f'    {expr_to_string(fld.type)};\r\n'
        else:
            returnString += f'header {hdr.name} {{\r\n'
            for fld in hdr.fields:
                returnString += f'    {expr_to_string(fld)};\r\n'
        returnString += f'}}\r\n'
        returnString += "\r\n"

    returnString += f'struct headers {{\r\n'
    for hdrinst in hlir.header_instances.filter(lambda hdrinst: hdrinst.name != 'all_metadatas_t'):
        returnString += f'    {hdrinst.urtype.name} {hdrinst.name};\r\n'
    returnString += f'}}\r\n'
    returnString += "\r\n"


    for parser in hlir.parsers:
        params = ', '.join(f'{param.direction} {param.urtype.name} {param.name}' for param in parser.type.applyParams.parameters)
        # breakpoint()
        parserHeaderName = parser.type.applyParams.parameters[1].name
        
        returnString += f'parser {parser.type.name}({params}) {{\r\n'
        for state in parser.states:
            if state.name in ('accept', 'reject'):
                continue

            returnString += f'    state {state.name} {{\r\n'
            for stateComponent in state.components:
                if stateComponent.node_type == "AssignmentStatement":
                    returnString += print_body_component(3+1,stateComponent)
                elif stateComponent.call == 'extract_header':
                    returnString += f'        packet.extract(\r\n'
                    for argument in stateComponent.methodCall.arguments:
                        returnString += f'          {argument.expression.expr.path.name}.{argument.expression.hdr_ref.name}\r\n'
                    returnString += f'        );\r\n'
                else:
                    returnString += "\r\n"
                    #normal call/assignment
                        
            if state.selectExpression.node_type == "PathExpression":
                returnString += f'        transition {state.selectExpression.path.name};\r\n'
            else:
                returnString += f'        transition select({parserHeaderName}.{state.selectExpression.select.components[0].expr.member}.{state.selectExpression.select.components[0].fld_ref.name}){"{"}\r\n'
                for case in state.selectExpression.selectCases:
                    if(case.keyset.node_type == 'DefaultExpression'):
                        returnString += f'          default:{case.state.path.name};\r\n'
                    else:
                        if case.keyset.node_type == "ListExpression":
                            vals = ', '.join(f'{value.value}' for value in case.keyset.components)
                            returnString += f'          ({vals}):{case.state.path.name};\r\n'
                        else:
                            returnString += f'          {case.keyset.value}:{case.state.path.name};\r\n'
                if state.selectExpression.select.components[0].fld_ref.name == 'accept':
                    returnString += f'        transition accept;\r\n'
                returnString += '        }\r\n'
            returnString += f'    }}\r\n'
        returnString += f'}}\r\n'
        returnString += "\r\n"

    for ctl in hlir.controls:
        params = ', '.join(f'{param.direction} {param.urtype.name} {param.name}' for param in ctl.type.applyParams.parameters)

        returnString += f'control {ctl.type.name}({params}) {{\r\n'

        for variable in ctl.controlLocals:
            if variable.node_type == "Declaration_Variable":
                returnString += f'        {expr_to_string(variable)};\r\n'

        for action in ctl.actions:
            # TODO
            params = ', '.join(f'{expr_to_string(param.type)} {param.name}' for param in action.parameters.parameters.vec)
        
            returnString += f'    action {action.name}({params}) {{\r\n'
            for comp in action.body.components:
                returnString += print_body_component(2, comp)
            returnString += f'    }}\r\n'

        for table in ctl.tables:
            returnString += f'    table {table.name} {{\r\n'

            returnString += f'        key = {{\r\n'
            for keyelem in table.key.keyElements:
                returnString += f'            {expr_to_string(keyelem.expression)}: {keyelem.matchType.path.name};\r\n'
            returnString += f'        }}\r\n'

            returnString += f'        actions = {{\r\n'
            for name in table.actions.map('action_object.name'):
                returnString += f'            {name};\r\n'
            returnString += f'        }}\r\n'

            if 'size' in table:
                returnString += f'        size = {expr_to_string(table.size.expression)};\r\n'

            if 'default_action' in table:
                returnString += f'        default_action = {expr_to_string(table.default_action.expression)};\r\n'

            returnString += f'    }}\r\n'

        returnString += f'    apply {{\r\n'
        for comp in ctl.body.components:
            returnString += print_body_component(2, comp)
        returnString += f'    }}\r\n'

        returnString += f'}}\r\n'
        returnString += "\r\n"
    
        
    for instance in hlir.decl_instances:
        params = ',\r\n'.join(f'{argument.expression.type.name}()' for argument in instance.arguments)
        returnString += f'{expr_to_string(instance.type)}({params}) {instance.name}; \r\n'



    return returnString

