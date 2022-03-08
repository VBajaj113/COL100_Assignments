from sys import exit  # For stopping the program when necessary

#Required lists
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
    #To handle all operations and to make the instruction list

    def __init__(self, token, tabs=0, type_s="while", address=-1, TABS = TABS, DATA = DATA):
        #To initialise an object
        self.exp = token        #stores the expression
        self.tabs = tabs        #stores the tab number
        self.type = type_s      #stores the type of the statement
        self.addr = address     #stores the branching address
        self.tablist = TABS     #stores the TABS list
        self.datalist = DATA    #stores the DATA list
    

    def __repr__(self):     #For correct representation when printing the list
        try:
            if self.type == "branch":
                return self.type + " " + str(self.addr)
            elif self.type == "Expression":
                return " ".join(self.exp)
            else:
                return " ".join([self.type, self.exp[1], self.exp[2], str(self.addr)])
        except:
            exit("Please use correct syntax.")


    def while_help(self, lines, INSTRUCTION, i):
        #To help with the addition of branch and while statements correctly in INSTRUCTION
        #uses recursion for nested while loops
        
        #Inputs: 
        #lines, the list of statements, the INSTRUCTION list and the index i of while loop

        #Returns:
        #The index where the while loop ended

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
            exit("Error: Please enter the syntax in the correct format.")

        j = i + 1
        while j < n:
            if TABS[j] > TABS[i]:
                if lines[j].split()[0] == "while":  #Identified nested loop

                    pointer = Instructions(lines[j].split(), self.tablist[j])
                    j = pointer.while_help(lines, INSTRUCTION, j)

                    if j < n and TABS[j] <= TABS[i]:        #If the outer loop ends on the same line
                        self.addr = 1+len(INSTRUCTION)      #as the nested one, the to not skip a line
                        self.exp[-1] = str(1+len(INSTRUCTION))
                        temp = Instructions([str(i)], 0, "branch", i)
                        INSTRUCTION.append(temp)
                        return j
                else:
                    #Adds the normal expressions to the list
                    pointer = Instructions(lines[j].split(),self.tablist[j],"Expression")
                    INSTRUCTION.append(pointer)
                    j+=1

            else:
                break
        
        #Adds the branch statement with correct attributes
        self.addr = 1 + j + nested
        self.exp[-1]=str(1+j+nested)
        temp = Instructions([str(i)], 0, "branch", i)
        INSTRUCTION.append(temp)
        return j + nested


    def rectify(self, INSTRUCTIONS):
        #Changes the while statements in the list to BLE,BLT,BE types

        #Input: The instruction list

        #Output = None

        for i in range(len(INSTRUCTIONS)):
            pointer = INSTRUCTION[i]
            if pointer.type =="while":  #Identified the while statement
                if len(pointer.exp)==5:
                    try:
                        pointer.type = WHILE_BI[BINARY_OPERATOR.index(pointer.exp[2])]
                        pointer.binary_correct()    #Helper funtion for handling the long case
                    except:
                        exit("Error: Please use correct syntax.")

                elif len(pointer.exp)==4:
                    try:
                        pointer.exp[0]=WHILE_UN[UNARY_OPERATOR.index(pointer.exp[1])]
                    except:
                        exit("Error: Please use correct syntax.")
                
                elif len(pointer.exp)==3:
                    pointer.exp[0]="Expression"
                        
                else:
                    exit("Error: Please use correct syntax")  #raise error
    

    def binary_correct(self):
        #Corrects the while statement in the instructions by calling more helper functions

        #Input: the self pointer of the while statement

        #Output: None

        if self.type=="BLE":
            if self.exp[2]==">":
                self.case1()
            else:
                self.case2()    #Need to exchange the variables
        
        elif self.type=="BLT":
            if self.exp[2]==">=":
                self.case1()
            else:
                self.case2()    #Need to exchange the variables
        
        elif self.type == "BE":
            self.case_equal()
        
        else:
            self.case4()    #Made to handle and, or etc, but now handles errors


    def case1(self):
        #Changes the expression of the while statement as required

        #Input: The self pointer of the while statement

        #Output: None

        self.exp[2]=self.exp[3]
        self.exp[3]=self.exp[4]
        self.exp=self.exp[:-1]      #Removes the semicolon

    def case2(self):
        #Changes the expression of the while statement as required

        #Input: The self pointer of the while statement

        #Output: None

        self.case1()
        self.exp[1], self.exp[2] = self.exp[2], self.exp[1] #Exchanges the variables

    def case4(self):    #Error case
        exit("Error: Please enter the syntax in the correct format.")

    def case_equal(self):
        #Specially for BE, as there were some problems in implementing it the original way

        #Input: Slef statement of the while loop

        #output: calls the case 1 for further improvement after working

        if self.exp[2]=="==":
            self.exp[0] = "BEE"
        return self.case1()

    
    def ispresentbool(self, element):
        #To identify that the datalist has the element in boolean form

        #Input: The element tot be found

        #Output: The index of the element, if found in the data list

        for i in range(len(self.datalist)):
            if self.datalist[i] == element and type(self.datalist[i]) == bool:
                return i
        return -1

    def ispresentint(self, element):
        #To identify that the datalist has the element in integer form

        #Input: The element to be found

        #Output: The index of the element, if found in the data list

        for i in range(len(self.datalist)):
            if self.datalist[i] == element and type(self.datalist[i])==int:
                return i
        return -1

    def ispresentintuple(self, element):
        #To identify that the datalist has the element in tuple form

        #Input: The element to be found

        #Output: The index of the element value, if found in the data list

        for i in range(len(self.datalist)):
            try:
                if self.datalist[i][0] == element:
                    return i
            except:
                continue
        return -1

    def variablecheck(self, s):
        #Checks that the variable name only contains letters

        #Input: The name to be checked

        #Output: True if the name is correct, False otherwise

        for i in s:
            if ord(i) < 65 or ord(i) > 122 or (ord(i) > 90 and ord(i) < 97):
                return False
        return True


    def INTERPRET(self, exp, k):
        #Interprets the expressions
        
        #Input: The expression to be evaluated and the index at which the exp is in instruction list

        #Output: The next index where the index should be moved, along with calculating the expression
        #and changing the data list accordingly along with checking the fact that the loop iteration
        #is completed or not

        if self.type in WHILE_BI or self.type in WHILE_UN or self.type=="branch":
            #For interpreting the while and brach statements
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

            return  k+1, False  #The next index to be moved to and whether loop iteration is done


    def variable_value_special(self, expression):
        #Checks the variable values for the while loops

        #Input: The expression term for which value are to be substituted

        #Returns the updated expression and the boolean tellin whether while iteration is completed

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
        #To help running the execute funtion, calculates the next position of the index from
        #the branch and while statements

        #Inputs: the expression to be evakuated and the current index

        #Output: the new index and whether while loop is completed or not

        temp, boule = self.variable_value_special(exp[:])

        if not boule:      #Implies the elements are not boolean 
            #Checking case wise
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

            else:   #Branch statement
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


    def OUTPUT(self):  
        #For printing the output after every iteration

        #Returns Nothing
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


#-------------------------------------------------------------------------------------#
#Taking input from the file

lines = []          #Stores the lines to be evaluated

with open('D:\IITD\Current\COL100\Assignment\input_file.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    #Added the value of the tabs in the tab list
    statement = lines[i]
    TABS.append(max(statement.count("    "), statement.count("\t")))


n = len(lines)
i = 0
while i<n:
    #Updates the Instruction List
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

pointer.rectify(INSTRUCTION)    #Updates the types of the while statements

print(INSTRUCTION)


#----------------------------------------------------------------------------#
#Execution

i=0     #counter

while i < len(INSTRUCTION): #Execution
    pointer = INSTRUCTION[i]
    
    if pointer.exp[0]=="while":
        pointer.exp[0] = pointer.type
    expression = pointer.exp[:]
    
    i, boule = pointer.INTERPRET(expression, i)
    if pointer.type == "branch":
        pointer.OUTPUT()

pointer.OUTPUT()        #The final output after running thrugh all the instruction list

