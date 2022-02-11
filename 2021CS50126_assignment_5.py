DATA = []

def ispresentintbool(DATA,element):
    i=0
    while i<len(DATA):
        if DATA[i]==element:
            return True,i
        i+=1
    return False,-1

def ispresentintuple(DATA, element):
    i=0
    while i<len(DATA):
        try:
            if DATA[i][0]==element:
                return True,i
        except:
            continue
        i+=1
    return False,-1

def INTERPRET(token, DATA):
    if len(token)==3:
        new_var = token[0]
        term1=token[2]

        checkterm = ispresentintuple(DATA,term1)
        if checkterm[0]:
            checkvar = ispresentintuple(DATA, new_var)
            if checkvar[0]:
                DATA[checkvar[1]]=(new_var,DATA[checkterm[1]][1])
            else:                
                DATA.append((new_var,DATA[checkterm[1]][1]))
        else:    
            answer = ["Error:", term1, "is not defined yet."]
            return " ".join(answer)
    
    elif len(token)==4:
        new_var=token[0]
        term1=token[3]

        try:
            term1=int(term1)
            value=eval(token[2]+token[3])
            checkterm=ispresentintbool(DATA,term1)
            if not checkterm[0]:
                DATA.append(term1)
            checkvalue=ispresentintbool(DATA,value)
            checkvar=ispresentintuple(DATA,new_var)
            if not checkvalue[0]:
                DATA.append(value)
                if checkvar[0]:
                    DATA[checkvar[1]]=(new_var,len(DATA)-1)
                else:
                    DATA.append((new_var,len(DATA)-1))
            else:
                if checkvar[0]:
                    DATA[checkvar[1]]=(new_var,checkvalue[1])
                else:
                    DATA.append((new_var,len(DATA)-1))
                
        except:

