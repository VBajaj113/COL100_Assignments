DATA = []
BINARY_OPERATOR = ["+","-","*","/",">","<",">=","<=","==","!=","and","or"]
UNARY_OPERATOR = ["-","not"]

def ispresentbool(DATA,element):
    for i in range(len(DATA)):
        if DATA[i]==element and type(DATA[i])==bool:
            return i
    return -1

def ispresentint(DATA,element):
    for i in range(len(DATA)):
        if DATA[i]==element:
            return i
    return -1

def ispresentintuple(DATA, element):
    for i in range(len(DATA)):
        try:
            if DATA[i][0]==element:
                return i
        except:
            continue
    return -1

def INTERPRET(expression, DATA):
    new_var = expression[0]
    for i in range(2,len(expression)):
        term = expression[i]
        bool=False

        if term in UNARY_OPERATOR or term in BINARY_OPERATOR:
            continue

        elif  term=="True":
            bool=True
            if ispresentbool(DATA,True)==-1:
                DATA.append(True)

        elif term=="False":
            bool=True
            if ispresentbool(DATA,False)==-1:
                DATA.append(False)

        else:
            try:
                term=int(term)
                if ispresentint(DATA,term)==-1:
                    DATA.append(term)
            except:
                index=ispresentintuple(DATA,term)
                if index==-1:
                    return " ".join(["Error: variable",term,"is not defined"])
                else:
                    expression[i]=str(DATA[DATA[index][1]])
    
    value = eval("".join(expression[2:]))
    index=ispresentintuple(DATA,new_var)
    if bool:
        index2=ispresentbool(DATA,value)
    else:
        index2=ispresentint(DATA,value)
    
    if index2==-1:
        DATA.append(value)
        index2=len(DATA)-1
    
    if index==-1:
        DATA.append((new_var,index2))
    else:
        DATA[index]=(new_var,index2)

    return "next"


lines = [] # initalise to empty list
with open('D:\IITD\Current\COL100\Assignment\input_file.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
print (lines)
for statement in lines: # each statement is on a separate line
    token_list = statement.split() # split a statement into a list of tokens
    print ("Tokens: ", token_list)
    if INTERPRET(token_list,DATA)!="next":
        break
# now process each statement
print(DATA)