from sys import exit  # For stopping the program when necessary


DATA = []
INSTRUCTION = []
TABS = []
BINARY_OPERATOR = ["+", "-", "*", "/", ">", "<",">=", "<=", "==", "!=", "and", "or", "//"]
WHILE_BI = [None, None, None, None, "BLE", "BLE", "BLT", "BLT", "BE", "BE", "AND", "OR", None]
UNARY_OPERATOR = ["-", "not"]
WHILE_UN = [None, "NOT"]
STR_BOOL = ['True', 'False']
BOOL = [True, False]


class Instructions:
    def __init__(self, token, tabs=0, type_s="while", address=-1, TABS = TABS, DATA = DATA):
        #To initialise an object
        self.exp = token        #stores the expression
        self.tabs = tabs        #stores the tab number
        self.type = type_s      #stores the type of the statement
        self.addr = address     #stores the branching address
        self.tablist = TABS     #stores the TABS list
        self.datalist = DATA    #stores the DATA list
    

    def __repr__(self):     #For correct representation when printing the list
        if self.type == "branch":
            return self.type + " " + str(self.addr)
        elif self.type == "Expression":
            return " ".join(self.exp)
        else:
            return " ".join([self.type, self.exp[1], self.exp[2], str(self.addr)])


    def while_help(self, lines, INSTRUCTION, i):
        #To help with the addition of branch and while statements correctly in INSTRUCTION
        
        n = len(lines)
        nested = 0
        INSTRUCTION.append(self)

        j = i + 1
        while j < n:    #Checks how many nested while loops are there
            if TABS[j] > TABS[i]:
                if lines[j].split()[0] == "while":
                    nested+=1
            else:
                break
            j += 1

        if j == i + 1:  #When there is no statement in the while body (Wrong indent)
            exit("Please enter the syntax in the correct format.")

        j = i + 1
        while j < n:
            if TABS[j] > TABS[i]:
                if lines[j].split()[0] == "while":  #For handling the nested while loops

                    pointer = Instructions(lines[j].split(), self.tablist[j])
                    j = pointer.while_help(lines, INSTRUCTION, j)

                    if j < n and TABS[j] <= TABS[i]:
                        self.addr = 1+len(INSTRUCTION)
                        self.exp[-1] = str(1+len(INSTRUCTION))
                        temp = Instructions([str(i)], 0, "branch", i)
                        INSTRUCTION.append(temp)
                        return j
                else:
                    pointer = Instructions(lines[j].split(),self.tablist[j],"Expression")
                    INSTRUCTION.append(pointer)
                    j+=1

            else:
                break

        self.addr = 1 + j + nested
        self.exp[-1]=str(1+j+nested)
        temp = Instructions([str(i)], 0, "branch", i)
        INSTRUCTION.append(temp)
        return j + nested


    def rectify(self, INSTRUCTIONS):
        for i in range(len(INSTRUCTIONS)):
            pointer = INSTRUCTION[i]
            if pointer.type =="while":
                if len(pointer.exp)==5:
                    pointer.type = WHILE_BI[BINARY_OPERATOR.index(pointer.exp[2])]
                    pointer.binary_correct()

                elif len(pointer.exp)==4:
                    pointer.exp[0]=WHILE_UN[UNARY_OPERATOR.index(pointer.exp[1])]
                
                elif len(pointer.exp)==3:
                    pointer.exp[0]="Expression"
                        
                else:
                    exit()  #raise error
    

    def binary_correct(self):
        if self.type=="BLE":
            if self.exp[2]==">":
                self.case1()
            else:
                self.case2()
        
        elif self.type=="BLT":
            if self.exp[2]==">=":
                self.case1()
            else:
                self.case2()
        
        elif self.type == "BE":
            self.case_equal()
        
        else:
            self.case4()


    def case1(self):
        self.exp[2]=self.exp[3]
        self.exp[3]=self.exp[4]
        self.exp=self.exp[:-1]

    def case2(self):
        self.case1()
        self.exp[1], self.exp[2] = self.exp[2], self.exp[1]

    def case4(self):
        pass

    def case_equal(self):
        if self.exp[2]=="==":
            self.exp[0] = "BEE"
        return self.case1()


    
    def ispresentbool(self, element):
        for i in range(len(self.datalist)):
            if self.datalist[i] == element and type(self.datalist[i]) == bool:
                return i
        return -1

    def ispresentint(self, element):  # Checks whether element is present in DATA
        for i in range(len(self.datalist)):
            if self.datalist[i] == element and type(self.datalist[i])==int:
                return i
        return -1

    def ispresentintuple(self, element):    # Checks whether element is present in a tuple in DATA
        for i in range(len(self.datalist)):
            try:
                if self.datalist[i][0] == element:
                    return i
            except:
                continue
        return -1

    def variablecheck(self, s):  # Checks whether name of variable contains only letters
        for i in s:
            if ord(i) < 65 or ord(i) > 122 or (ord(i) > 90 and ord(i) < 97):
                return False
        return True


    def INTERPRET(self, exp, k):
        # Interprets the expressions
        if self.type in WHILE_BI or self.type in WHILE_UN or self.type=="branch":
            return self.while_run(exp, k)

        else:
        # Errors
            if len(exp) > 5 or len(exp) < 3:  # Not allowed lengths in this assignment
                exit("Error: Please enter the expression in the specified syntax")
            elif exp[1] != "=":  # The variable is of multiple words
                exit("Error: Please enter the expression in the specified syntax")
            # Not allowed operators
            elif len(exp) == 4 and exp[2] not in UNARY_OPERATOR:
                exit("Error: Please enter the expression in the specified syntax")
            elif len(exp) == 5 and (exp[3] not in BINARY_OPERATOR or exp[2] in \
                BINARY_OPERATOR or exp[4] in BINARY_OPERATOR):  # Not allowed expression when expression length is 5
                exit("Error: Please enter the expression in the specified syntax")

            new_var = exp[0]  # Represents the variable
            if not self.variablecheck(new_var):
                # Checks variable name is allowed
                exit("Error: Variable name '"+new_var+"' not allowed")

            for i in range(2, len(exp)):
                # Changes the variable in the expression to strings type indicating its value
                # and leaves the operators unchanged. Also adds the elements to DATA list if
                # they are not present initially.

                term = exp[i]
                boule = False

                if term == "/":
                    exp[i] = "//"  # To work it with eval()
                elif term in UNARY_OPERATOR or term in BINARY_OPERATOR:
                    continue
                elif term == "True":
                    boule = True
                    if self.ispresentbool(True) == -1:
                        self.datalist.append(True)
                elif term == "False":
                    boule = True
                    if self.ispresentbool(False) == -1:
                        self.datalist.append(False)
                else:
                    try:  # Checks if the term is a string of integer or variable and handles it
                        term = int(term)
                        if self.ispresentint(term) == -1:
                            self.datalist.append(term)
                    except:
                        index = self.ispresentintuple(term)
                        if index == -1:
                            # Error as variable is not defined.
                            exit("".join(["Error: variable '", term, "' is not defined"]))
                        else:
                            # Changes the variables to their values
                            exp[i] = str(self.datalist[self.datalist[index][1]])

            try:
                value = eval(" ".join(exp[2:]))  # Evaluates the rhs
            except ZeroDivisionError:
                exit("Error: Trying to divide by 0")
            except:
                exit("Error: Please enter the expression in the specified syntax")

            if boule:  # If the rhs is boolean
                index2 = self.ispresentbool(value)
            else:
                index2 = self.ispresentint(value)  # rhs is integer

            if index2 == -1:  # rhs is integer
                self.datalist.append(value)  # Adds rhs to DATA
                index2 = len(self.datalist)-1  # Index of rhs

            # Checks whether the lhs is already in DATA
            index = self.ispresentintuple(new_var)

            if index == -1:  # lhs not in DATA
                self.datalist.append((new_var, index2))
            else:
                self.datalist[index] = (new_var, index2)

            return  k+1, False


    def variable_value_special(self, expression):
        boule = False
        for i in range(1, len(expression)-1):
            # Changes the variable in the expression to strings type indicating its value
            # and leaves the operators unchanged. Also adds the elements to DATA list if
            # they are not present initially.

            term = expression[i]
            boule = False

            if term == "True":
                boule = True
                if self.ispresentbool(True) == -1:
                    self.datalist.append(True)
            elif term == "False":
                boule = True
                if self.ispresentbool(False) == -1:
                    self.datalist.append(False)
            else:
                try:  # Checks if the term is a string of integer or variable and handles it
                    term = int(term)
                    if self.ispresentint(term) == -1:
                        self.datalist.append(term)
                except:
                    index = self.ispresentintuple(term)
                    if index == -1:
                        # Error as variable is not defined.
                        exit("".join(["Error: variable '", term, "' is not defined"]))
                    else:
                        # Changes the variables to their values
                        expression[i] = str(self.datalist[self.datalist[index][1]])
        return expression, boule


    def while_run(self, exp, i):
        temp, boule = self.variable_value_special(exp[:])
        if not boule:
            if temp[0] == "BLE":
                if int(temp[1]) <= int(temp[2]):
                    return self.addr, True
                else:
                    return i+1, False
            elif temp[0] == "BLT":
                if int(temp[1]) < int(temp[2]):
                    return self.addr, True
                else:
                    return i+1, False
            elif temp[0] == "BE":
                if (temp[1])==(temp[2]):
                    return self.addr, True
                else:
                    return i+1, False
            elif temp[0]=="BEE":
                if (temp[1])==(temp[2]):
                    return i + 1, False
                else:
                    return self.addr, True
            else:
                return int(temp[-1]),False
        else:
            if temp[0] == "BLE":
                if BOOL[STR_BOOL.index(temp[1])] <= BOOL[STR_BOOL.index(temp[2])]:
                    return self.addr, True
                else:
                    return i+1, False
            elif temp[0] == "BLT":
                if BOOL[STR_BOOL.index(temp[1])] < BOOL[STR_BOOL.index(temp[2])]:
                    return self.addr, True
                else:
                    return i+1, False
            elif temp[0] == "BE":
                if BOOL[STR_BOOL.index(temp[1])]==BOOL[STR_BOOL.index(temp[2])]:
                    return self.addr, True
                else:
                    return i+1, False
            elif temp[0]=="BEE":
                if BOOL[STR_BOOL.index(temp[1])]==BOOL[STR_BOOL.index(temp[2])]:
                    return i + 1, False
                else:
                    return self.addr, True
            else:
                return int(temp[-1]),False


    def OUTPUT(self):  # For printing
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







lines = []
with open('D:\IITD\Current\COL100\Assignment\input_file.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    statement = lines[i]
    TABS.append(max(statement.count("    "), statement.count("\t")))


n = len(lines)
i = 0
while i<n:
    tabs = TABS[i]
    token_list = lines[i].split()
    fterm = token_list[0]

    if fterm == "while":
        if token_list[-1] != ":":
            exit("Please enter the syntax in the correct format.")
        pointer = Instructions(token_list, TABS[i])
        i = pointer.while_help(lines, INSTRUCTION, i)
    else:
        pointer = Instructions(token_list,tabs,"Expression")
        INSTRUCTION.append(pointer)
        i+=1

pointer.rectify(INSTRUCTION)
print(INSTRUCTION)


#Execution

i=0
while i < len(INSTRUCTION):
    pointer = INSTRUCTION[i]
    if pointer.exp[0]=="while":
        pointer.exp[0] = pointer.type
    expression = pointer.exp[:]
    
    i, boule = pointer.INTERPRET(expression, i)
    if pointer.type == "branch":
        pointer.OUTPUT()

pointer.OUTPUT()

