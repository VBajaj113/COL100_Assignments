from sys import exit  # For stopping the program when necessary


DATA = []
INSTRUCTION = []
TABS = []
BINARY_OPERATOR = ["+", "-", "*", "/", ">", "<",">=", "<=", "==", "!=", "and", "or", "//"]
WHILE_BI = [None, None, None, None, "BLE", "BLE", "BLT", "BLT", "BE", "BE", "AND", "OR", None]
UNARY_OPERATOR = ["-", "not"]
WHILE_UN = [None, "NOT"]


class Instructions:
    def __init__(self):
        self
    
    



def while_help(token_list, lines, INSTRUCTION, i):
    n=len(lines)
    nested = 0
    INSTRUCTION.append(token_list)

    j = i + 1
    while j < n:
        if TABS[j] > TABS[i]:
            if lines[j].split()[0] == "while":
                nested+=1
        else:
            break
        j += 1
                
    j = i + 1
    while j < n:
        if TABS[j] > TABS[i]:
            if lines[j].split()[0] == "while":
                j = while_help(lines[j].split(),lines, INSTRUCTION, j)
                if TABS[j]<=TABS[i]:
                    INSTRUCTION[i][-1]=str(1+len(INSTRUCTION))
                    INSTRUCTION.append(["branch", str(i)])
                    return j
            else:
                INSTRUCTION.append(lines[j].split())
                j+=1

        else:
            break
        
    INSTRUCTION[i][-1]=str(1+j+nested)
    INSTRUCTION.append(["branch", str(i)])
    return j + nested


def rectify(INSTRUCTIONS):
    for i in range(len(INSTRUCTIONS)):
        if INSTRUCTION[i][0]=="while":
            if len(INSTRUCTION[i])==5:
                INSTRUCTION[i][0]=WHILE_BI[BINARY_OPERATOR.index(INSTRUCTION[i][2])]
                binary_correct(INSTRUCTION,i)
                    
            elif len(INSTRUCTION[i])==4:
                INSTRUCTION[i][0]=WHILE_UN[UNARY_OPERATOR.index(INSTRUCTION[i][1])]
            
            elif len(INSTRUCTION[i])==3:
                INSTRUCTION[i][0]="Expression"
                
            else:
                exit()  #raise error


def case1(INSTRUCTION, i):
    INSTRUCTION[i][2]=INSTRUCTION[i][3]
    INSTRUCTION[i][3]=INSTRUCTION[i][4]
    INSTRUCTION[i]=INSTRUCTION[i][:-1]

def case2(INSTRUCTION, i):
    case1(INSTRUCTION,i)
    INSTRUCTION[i][1], INSTRUCTION[i][2] = INSTRUCTION[i][2], INSTRUCTION[i][1]

def case4(INSTRUCTION,i):
    pass

def case_equal(INSTRUCTION,i):
    pass

def binary_correct(INSTRUCTIONS,i):
    if INSTRUCTION[i][0]=="BLE":
        if INSTRUCTION[i][2]==">":
            case1(INSTRUCTION,i)
        else:
            case2(INSTRUCTION,i)
    
    elif INSTRUCTION[i][0]=="BLT":
        if INSTRUCTION[i][2]==">=":
            case1(INSTRUCTION,i)
        else:
            case2(INSTRUCTION,i)
    
    elif INSTRUCTION[i][0]=="BE":
        if INSTRUCTION[i][2]=="!=":
            case1(INSTRUCTION,i)
        else:
            case_equal(INSTRUCTION,i)
    
    else:
        case4(INSTRUCTION,i)


lines = []
with open('D:\IITD\Current\COL100\Assignment\input_file.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    statement = lines[i]
    TABS.append(max(statement.count("    "), statement.count("\t")))

n = len(lines)
i=0
while i<n:
    tabs = TABS[i]
    token_list = lines[i].split()
    fterm = token_list[0]

    if fterm == "while":
        i = while_help(token_list,lines,INSTRUCTION,i)
    else:
        INSTRUCTION.append(token_list)
        i+=1
rectify(INSTRUCTION)


print(INSTRUCTION)



def OUTPUT():  # For printing
    GARBAGE = []
    USED_INDEX = []  # Stores the values of indices which are not garbage

    for i in range(len(DATA)):
        try:
            # Prints the variables and values
            print(DATA[i][0], "=", DATA[DATA[i][1]])
            # Adds the index which are not garbage
            USED_INDEX.extend([i, DATA[i][1]])
        except:
            continue

    for i in range(len(DATA)):  # Adds the garbage elements to the list
        if i not in USED_INDEX:
            GARBAGE.append(DATA[i])

    print(GARBAGE)

# Checks whether the element is present in DATA and is of type bool
def ispresentbool(DATA, element):
    for i in range(len(DATA)):
        if DATA[i] == element and type(DATA[i]) == bool:
            return i
    return -1

def ispresentint(DATA, element):  # Checks whether element is present in DATA
    for i in range(len(DATA)):
        if DATA[i] == element:
            return i
    return -1

def ispresentintuple(DATA, element):    # Checks whether element is present in a tuple in DATA
    for i in range(len(DATA)):
        try:
            if DATA[i][0] == element:
                return i
        except:
            continue
    return -1

def variablecheck(s):  # Checks whether name of variable contains only letters
    for i in s:
        if ord(i) < 65 or ord(i) > 122 or (ord(i) > 90 and ord(i) < 97):
            return False
    return True

def INTERPRET(expression, DATA, k):
    # Interprets the expressions
    if expression[0] in WHILE_BI or expression[0] in WHILE_UN or expression[0]=="branch":
        return execute(expression, DATA, k)

    else:
    # Errors
        if len(expression) > 5 or len(expression) < 3:  # Not allowed lengths in this assignment
            exit("Error: Please enter the expression in the specified syntax")
        elif expression[1] != "=":  # The variable is of multiple words
            exit("Error: Please enter the expression in the specified syntax")
        # Not allowed operators
        elif len(expression) == 4 and expression[2] not in UNARY_OPERATOR:
            exit("Error: Please enter the expression in the specified syntax")
        elif len(expression) == 5 and (expression[3] not in BINARY_OPERATOR or expression[2] in BINARY_OPERATOR
                                    or expression[4] in BINARY_OPERATOR):  # Not allowed expression when expression length is 5
            exit("Error: Please enter the expression in the specified syntax")

        new_var = expression[0]  # Represents the variable
        if not variablecheck(new_var):
            # Checks variable name is allowed
            exit("Error: Variable name '"+new_var+"' not allowed")

        for i in range(2, len(expression)):
            # Changes the variable in the expression to strings type indicating its value
            # and leaves the operators unchanged. Also adds the elements to DATA list if
            # they are not present initially.

            term = expression[i]
            bool = False

            if term == "/":
                expression[i] = "//"  # To work it with eval()
            elif term in UNARY_OPERATOR or term in BINARY_OPERATOR:
                continue
            elif term == "True":
                bool = True
                if ispresentbool(DATA, True) == -1:
                    DATA.append(True)
            elif term == "False":
                bool = True
                if ispresentbool(DATA, False) == -1:
                    DATA.append(False)
            else:
                try:  # Checks if the term is a string of integer or variable and handles it
                    term = int(term)
                    if ispresentint(DATA, term) == -1:
                        DATA.append(term)
                except:
                    index = ispresentintuple(DATA, term)
                    if index == -1:
                        # Error as variable is not defined.
                        exit(
                            "".join(["Error: variable '", term, "' is not defined"]))
                    else:
                        # Changes the variables to their values
                        expression[i] = str(DATA[DATA[index][1]])

        try:
            value = eval(" ".join(expression[2:]))  # Evaluates the rhs
        except ZeroDivisionError:
            exit("Error: Trying to divide by 0")
        except:
            exit("Error: Please enter the expression in the specified syntax")

        if bool:  # If the rhs is boolean
            index2 = ispresentbool(DATA, value)
        else:
            index2 = ispresentint(DATA, value)  # rhs is integer

        if index2 == -1:  # rhs is integer
            DATA.append(value)  # Adds rhs to DATA
            index2 = len(DATA)-1  # Index of rhs

        # Checks whether the lhs is already in DATA
        index = ispresentintuple(DATA, new_var)

        if index == -1:  # lhs not in DATA
            DATA.append((new_var, index2))
        else:
            DATA[index] = (new_var, index2)

        return  k+1, False


def variable_value_special(expression, DATA):
    for i in range(1, len(expression)-1):
        # Changes the variable in the expression to strings type indicating its value
        # and leaves the operators unchanged. Also adds the elements to DATA list if
        # they are not present initially.

        term = expression[i]
        bool = False

        if term == "True":
            bool = True
            if ispresentbool(DATA, True) == -1:
                DATA.append(True)
        elif term == "False":
            bool = True
            if ispresentbool(DATA, False) == -1:
                DATA.append(False)
        else:
            try:  # Checks if the term is a string of integer or variable and handles it
                term = int(term)
                if ispresentint(DATA, term) == -1:
                    DATA.append(term)
            except:
                index = ispresentintuple(DATA, term)
                if index == -1:
                    # Error as variable is not defined.
                    exit("".join(["Error: variable '", term, "' is not defined"]))
                else:
                    # Changes the variables to their values
                    expression[i] = str(DATA[DATA[index][1]])
    return expression


def execute(expression, DATA, i):
    temp = variable_value_special(expression[:],DATA)

    if temp[0]=="BLE":
        if int(temp[1])<=int(temp[2]):
            return int(temp[3]), True
        else:
            return i+1, False
    elif temp[0]=="BLT":
        if int(temp[1])<int(temp[2]):
            return int(temp[3]), True
        else:
            return i+1, False
    elif temp[0]=="BE":
        return
    else:
        return int(temp[-1]),False

i=0
while i < len(INSTRUCTION):
    expression = INSTRUCTION[i][:]
    i, bool = INTERPRET(expression, DATA, i)
    if bool==True:
        OUTPUT()
    
OUTPUT()
