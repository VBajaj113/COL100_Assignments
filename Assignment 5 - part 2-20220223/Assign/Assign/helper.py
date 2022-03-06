def remove_leading_spaces(term):
    i = 0
    n = len(term)
    
    while (i<n) and (term[i] == " "):
        i+=1
    return term[i:]

def remove_trailing_spaces(term):
    n = len(term)
    i = n - 1 

    while (i>=0) and (term[i] == " "):
        i-=1
    return term[:i+1]
