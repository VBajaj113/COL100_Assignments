def add(reg1, reg2):
    return reg1 + reg2 

def sub(reg1, reg2):
    return reg1 - reg2 

def mul(reg1, reg2):
    return reg1 * reg2 

def div(reg1, reg2):
    return reg1 / reg2 

def grt(reg1, reg2):
    return reg1 > reg2 

def less(reg1, reg2):
    return reg1 < reg2 

def greq(reg1, reg2):
    return reg1 >= reg2 

def lez(reg1, reg2):
    return reg1 <= reg2 

def equal(reg1, reg2):
    return reg1 == reg2 

def unequal(reg1, reg2):
    return reg1 != reg2 

def AND(reg1, reg2):
    return reg1 and reg2 

def OR(reg1, reg2):
    return reg1 or reg2 

def negate(reg1, reg2):
    return -reg2 

def NOT(reg1, reg2):
    return not reg2 
    
operator_list = ["+", "-", "*", "/", ">=", "<=", ">", "<", "==", "!=", " and ", " or "]
op_func_list = [add, sub, mul, div, greq, lez, grt, less, equal, unequal, AND, OR]