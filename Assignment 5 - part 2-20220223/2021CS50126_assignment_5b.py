from sys import exit  # For stopping the program when necessary

DATA = []
INSTRUCTION = []
TABS = []
BINARY_OPERATOR = ["+", "-", "*", "/", ">", "<",">=", "<=", "==", "!=", "and", "or", "//"]
UNARY_OPERATOR = ["-", "not"]
WHILE_BI = [None,None,None,None,"BLE","BLT","BLT","BLE","BE","BE","AND","OR",None]
WHILE_UN = ["SUB","NOT"]

class Instructions:
    def __init__(self, token_list, tabs, type_statement=None, addr=-1):
        self.type = type_statement
        self.exp = token_list
        self.tabs = tabs
        self.body = 0
        if addr > -1:
            self.destination_addr = addr

    def analyse_type(self):
        if self.exp[0] != "while":
            self.type = ""

        elif len(self.exp)==5:
            for i in range(13):
                if BINARY_OPERATOR[i]==self.exp[3]:
                    self.type=WHILE_BI[i]
                    break

        elif len(self.exp)==4:
            for i in range(2):
                if UNARY_OPERATOR[i]==self.exp[2]:
                    self.type=WHILE_UN[i]
                    break
        
        elif len(self.exp)==3:
            self.type = "SOLO"

        else:
            exit("Error: Please enter the expression in the specified syntax")
        





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

def INTERPRET(expression, DATA):
    # Interprets the expressions

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

    return  # Returns nothing


lines = []  # initalise to empty list
with open('D:\IITD\Current\COL100\Assignment\input_file.txt') as f:
    lines = f.readlines()  # read all lines into a list of strings


for statement in lines:  # each statement is on a separate line
    tabs = 0
    while statement[tabs] == '\t':
        tabs += 1
    TABS.append(tabs)


for i in range(len(lines)):
    statement = lines[i]
    tabs = TABS[i]
    token_list = statement.split()  # split a statement into a list of tokens
    
    pointer = Instructions(token_list, TABS[i])
    pointer.analyse_type()

    loop_body=0
    for j in range(i+1, len(lines)):
        if TABS[j]>=TABS[i]:
            loop_body+=1
        else:
            break
    
    pointer.body = loop_body
    


print(INSTRUCTION)

