lines = [] # initalise to empty list
with open('D:\IITD\Current\COL100\Assignment\input_file.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
print (lines)
for statement in lines: # each statement is on a separate line
    tabs = 0
    while statement[tabs] == '\t':
        tabs += 1
    print ("tabs: ", tabs)
    token_list = statement.split() # split a statement into a list of tokens
    print ("Tokens: ", token_list)
# now process each statement
