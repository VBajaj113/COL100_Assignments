def INTERPRET(input_expression):
    DATA=[]
    BINARY_OPERATOR=['+','-','*','/','>','<','>=','<=','==','!=','and','or']
    UNARY_OPERATOR=['-','not']

    INDEX=0
    VARIABLE=""
    while (input_expression[INDEX]!=' '):
        VARIABLE+=input_expression[INDEX]
        INDEX+=1

    INDEX+=3

    if input_expression[INDEX] in UNARY_OPERATOR:
        if input_expression[INDEX]=='-':

        else:
            
    else:
        TERM1=""
        while (input_expression[INDEX] not in BINARY_OPERATOR or INDEX!=len(input_expression)):
            TERM1+=input_expression[INDEX]
            INDEX+=1

        if INDEX==len(input_expression):
            DATA.append(TERM1)
            DATA.append(VARIABLE,len(DATA)-1)
        else:
            operator=""



while True:
    input_expression=input()
    INTERPRET(input_expression)