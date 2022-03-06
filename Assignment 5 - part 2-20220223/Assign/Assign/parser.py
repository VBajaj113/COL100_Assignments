import helper
import operators 


def parse_while_statement(line):
    line = helper.remove_trailing_spaces(line)
    
    if line[-1] != ":":
        return False, (None, None, None, None)
    line = line[:-1]

    if line[:6] != "while ":
        return False, (None, None, None, None)
    expr = line[6:]
    expr = helper.remove_leading_spaces(expr)
    expr = helper.remove_trailing_spaces(expr)

    valid, type, reg1, op, reg2 = parse_expression(expr)
    if not valid:
        return False, (None, None, None, None)
    return True, (type, reg1, op, reg2) 

# Statement -> Variable = Expression
# Return Valid/Invalid, variable, (1/2/3, reg1, operator, reg2)
def parse_statement(line):
    i = 0
    n = len(line)

    equal_sign_found = False 
    equal_sign_position = -1

    while (i<n) and (not equal_sign_found):
        if line[i] == '=':
            equal_sign_found = True 
            equal_sign_position = i 
        i = i + 1
    
    if not equal_sign_found:
        return False, None, (None, None, None, None)
    
    variable = line[:equal_sign_position]
    expression = line[equal_sign_position+1:]

    variable = helper.remove_trailing_spaces(variable)
    expression = helper.remove_leading_spaces(expression)
    expression = helper.remove_trailing_spaces(expression)

    (valid, var) = parse_variable(variable)
    if not valid:
        return False, None, (None, None, None, None)
    
    (valid, type_expr, reg1, op, reg2) = parse_expression(expression)

    if not valid:
        return False, None, (None, None, None, None)

    return True, var, (type_expr, reg1, op, reg2)

# First Char should be alphabet 
# Only alphabet, numeral, _ allowed
def parse_variable(var):
    var = helper.remove_trailing_spaces(var) 
    n = len(var)
    i = 1

    if n == 0:
        return False, None 
    
    if (var[0] != '_') and (not var[0].isalpha()):
        return False, None 
    
    while i < n:
        if (var[i] != '_') and (not var[i].isalpha()) and (not var[i].isdigit()):
            return False, None 
        i+=1
    
    return True, var

# Term -> True 
#      -> False 
#      -> Variable 
#      -> Integer 
def parse_term(term):
    term = helper.remove_leading_spaces(term)
    term = helper.remove_trailing_spaces(term)

    if term == "True":
        return (True, True)
    if term == "False":
        return (True, False)
    
    if term.isnumeric():
        return (True, int(term))
    
    return parse_variable(term)

def check_term(expr):
    (valid, _) = parse_term(expr)
    return valid 

def check_unary_op(expr):
    if expr[0] == '-':
        return True 
    n = len(expr)
    if n < 5:
        return False 
    
    if expr[:4] == "not ":
        return True 
    return False

# Expression -> Term
#            -> Unary_Operator Term 
#            -> Term Binary_Operator Term 
# Return Valid/Invalid, 1/2/3, reg1, operator, reg2
def parse_expression(expr):
    expr = helper.remove_leading_spaces(expr)
    expr = helper.remove_trailing_spaces(expr)

    if len(expr) == 0:
        return False, None, None, None, None

    valid, val = parse_term(expr)
    if valid:
        return True, 1, val, None, None
    
    valid_unary = check_unary_op(expr)
    if valid_unary:
        return parse_unary(expr)
    
    return parse_binary(expr)

def parse_binary(expr):
    end_pos = -1
    start_pos = -1
    operator = None 

    for i in range(len(operators.operator_list)):
        pos = expr.find(operators.operator_list[i])
        if pos == -1:
            continue
        end_pos = pos
        start_pos = len(operators.operator_list[i]) + pos 
        operator = operators.op_func_list[i]
        break
    
    valid1, val1 = parse_term(expr[:end_pos])
    valid2, val2 = parse_term(expr[start_pos:])

    if valid1 and valid2:
        return True, 3, val1, operator, val2 
    else:
        return False, None, None, None, None


def parse_unary(expr):
    n = len(expr)

    if expr[0] == '-':
        valid, val = parse_term(expr[1:])
        if valid:
            return True, 2, None, operators.negate, val
        else:
            return False, None, None, None, None 
    term = expr[4:]
    valid, val = parse_term(term)
    if valid:
        return True, 2, None, operators.NOT, val
    else:
        return False, None, None, None, None 

# while True:
#     inp = input()
#     if inp == "exit":
#         break 
#     v, _ = parse_while_statement(inp)
#     if not v:
#         print(parse_statement(inp))
#     else:
#         print("While ", parse_while_statement(inp))
