lines = [] # initalise to empty list
with open('c:/Users/DELL/Desktop/Python/a.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
print (lines)
for statement in lines: # each statement is on a separate line
    token_list = statement.split() # split a statement into a list of tokens
    print ("Tokens: ", token_list)
# now process each statement
