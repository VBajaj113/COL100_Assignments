# lines = [] # initalise to empty list
# with open('/Users/kremlesis/Desktop/test.txt', 'r') as f:
#     lines = f.readlines() # read all lines into a list of strings
# print (lines)
# for statement in lines: # each statement is on a separate line
#     tabs = 0
#     # statement = statement.replace("    ", '\t')
#     while statement[tabs] == '\t':
#         tabs += 1
#     print ("tabs: ", tabs)
#     token_list = statement.split() # split a statement into a list of tokens
#     print ("Tokens: ", token_list)
# # now process each statement

import parser 
import classes
import operators 
import sys

def make_instr_list(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    instr_list = []
    for statement in lines:
        statement = statement.rstrip()
        tabs = 0
        while statement[tabs] == '\t':
            tabs+=1
        statement = statement[tabs:]
        # print(statement)
        valid, tup = parser.parse_while_statement(statement)
        if valid:
            instr_list.append((tabs, True, parser.parse_while_statement(statement)))
        else:
            instr_list.append((tabs, False, parser.parse_statement(statement)))
    
    valid = check_instr_list(instr_list)
    if not valid:
        return False, None 
    else:
        return True, instr_list 
    # print(valid)

def check_instr_list(instr_list):
    min_tab = 0 
    max_tab = 0
    n = len(instr_list)
    # print(instr_list)
    for i in range(n):
        tabs, isWhile, tup = instr_list[i]
        if not tup[0]:
            return False 
        
        if tabs < min_tab:
            return False 
        if tabs > max_tab:
            return False 
        
        if tabs < max_tab:
            max_tab = tabs 
        if isWhile:
            max_tab+=1
            min_tab = max_tab 
        else:
            min_tab = 0
    return True
        
def make_object_list(instr_list):
    while_list = []
    instr_object_list = []
    obj_count = 0

    for i in range(len(instr_list)):
        instr = instr_list[i]
        tab = instr[0]

        while len(while_list):
            o = while_list[-1]
            if o[0] >= tab:
                while_list.pop()
                instr_object_list.append(classes.Instruction(4, None, None, None, o[1].result))
                obj_count+=1
                o[1].result = obj_count 
            else:
                break




        if not instr[1]:
            expr = instr[2]
            res = expr[1]
            rhs = expr[2]
            obj = classes.Instruction(0, rhs[1], rhs[2], rhs[3], res)
        else:
            expr = instr[2][1]
            if expr[2] == operators.less:
                obj = classes.Instruction(1,expr[3], None, expr[1], obj_count)
            elif expr[2] == operators.unequal:
                obj = classes.Instruction(3, expr[1], None, expr[3], obj_count)
            elif expr[2] == operators.lez:
                obj = classes.Instruction(2, expr[3], None, expr[1], obj_count)
            elif expr[2] == operators.greq:
                obj = classes.Instruction(2, expr[1], None, expr[3], obj_count)
            elif expr[2] == operators.grt:
                obj = classes.Instruction(1, expr[1], None, expr[3], obj_count)
            else:
                print("Invalid While Syntax")
                sys.exit()   
            while_list.append((instr[0], obj))
        instr_object_list.append(obj)
        obj_count+=1 
    
    while len(while_list):
        o = while_list[-1]
        if o[0] >= 0:
            while_list.pop()
            instr_object_list.append(classes.Instruction(4, None, None, None, o[1].result))
            obj_count+=1
            o[1].result = obj_count  
        else:
            break 

    for i in instr_object_list:
        i.Print()    

    for i in instr_object_list:
        i.Print2()  
    
    return instr_object_list



def main():
    filename = "test2.txt"
    val, instr_list = make_instr_list(filename)

    for i in instr_list:
        print(i)
    print("Done\n")
    if not val:
        print("Syntax Error")
        sys.exit()
    i_list = make_object_list(instr_list)
    PC = 0

    n = len(i_list)
    data_list = []
    while PC < n:
        print("PC is ", PC)
        print(data_list)
        PC = i_list[PC].execute(PC, data_list)
    print(data_list)


    
if __name__ == "__main__":
    main()

# make_instr_list("test.txt")