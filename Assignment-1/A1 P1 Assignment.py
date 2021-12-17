### COL Assignment 1 ###
#----------------------#


#Part 1:

#Half Adder -- Helper for Full Adder
def hadd(a,b):
    #Addition of 2 bits

    #Parameters:
    #a: boolean -- the first bit
    #b: boolean -- the second bit

    #Returns: 2 element Tuple -- Boolean elements representing the bits
    #         of sum of a and b in reverse order
    
    #Logic:
    # 0 + 0 = 00
    # 1 + 0 = 01
    # 0 + 1 = 01
    # 1 + 1 = 10
    #We can see that the truth table for unit's digit is of XOR operator
    #and second digit is of AND operator.
    
    return (bool((a or b) and not (a and b)), bool(a and b))



#Full Adder
def add(a,b,c):
    #Addition of 3 bits

    #Parameters:
    #a: boolean -- the first bit
    #b: boolean -- the second bit
    #c: boolean -- the third bit

    #Returns: 2 Element Tuple with Boolean elements representing the bits
    #         of sum a+b+c in reverse order

    #Logic:
    # 00 + 0 = 00
    # 00 + 1 = 01
    # 01 + 0 = 01
    # 01 + 1 = 10
    # 10 + 0 = 10
    # 10 + 1 = 11
    #This time, the unit's digit is (a XOR b) XOR c and the second digit
    #is ((a AND b) OR (b AND c) OR (a AND c))
    
    (ab1,ab2)=hadd(a,b)     #ab1 = a XOR b, ab2 = a AND b
    (bc1,bc2)=hadd(b,c)     #bc1 = b XOR c, bc2 = b AND c
    (ca1,ca2)=hadd(c,a)     #ca1 = c XOR a, ca2 = c AND a
    
    (r0,r1)=hadd(c,ab1)     #r0 = ab1 XOR c = (a XOR b) XOR c; r1 = ab1 AND c
    
    return (bool(r0),bool(ab2 or ca2 or bc2))



#4-bit adder
def add4(a0,a1,a2,a3, b0,b1,b2,b3, c):
    #Adder for two 4 bit numbers and a carry digit

    #Parameters:
    #a0, a1, a2, a3 : boolean -- the bits of 4 bit numeral a3a2a1a0
    #b0, b1, b2, b3 : boolean -- the bits of 4 bit numeral b3b2b1b0
    #             c : boolean -- carry bit

    #Returns: 5 element Tuple with Boolean elements representing the bits of
    #         the sum a3a2a1a0 + b3b2b1b0 + c in reverse order

    #Logic: Repeatedly call the full adder function and update the carry bit.
    
    (r0,c) = add(a0,b0,c)
    (r1,c) = add(a1,b1,c)
    (r2,c) = add(a2,b2,c)
    (r3,c) = add(a3,b3,c)
    
    return (r0,r1,r2,r3,c)



#Comparator ( > )
def cmp(a0,a1,a2,a3, b0,b1,b2,b3):
    #Greater Than or '>' comparator between two 4 bit numbers

    #Parameters:
    #a0, a1, a2, a3 : boolean -- the bits of 4 bit numeral a3a2a1a0
    #b0, b1, b2, b3 : boolean -- the bits of 4 bit numeral b3b2b1b0

    #Returns: Boolean -- Whether a3a2a1a0 > b3b2b1b0 or not

    #Logic: For each group (ai, bi) in the order i=3 to i=0:
    #1) Find XOR of the two.
    #2) If XOR is 0, then move to next group as both the bits are same.
    #   If there is no next group, then both the numbers are same, so return False.
    #3) If XOR isn't 0, then there are 2 cases, either a==True, or a==False.
    #   If a==True ==> b==False, so return True ==> return a
    #   If a==False ==> b==True, so return False ==> return a

    if bool((a3 or b3) and not (a3 and b3)):
            return bool(a3)
    if bool((a2 or b2) and not (a2 and b2)):
            return bool(a2)
    if bool((a1 or b1) and not (a1 and b1)):
            return bool(a1)
    if bool((a0 or b0) and not (a0 and b0)):
            return bool(a0)
    return False



#Singe Bit Subtractor -- Helper for sub4
def sub(a1, b1, b):
    #Subtracts the two bits including the effect of borrow

    #Parameters:
    #a1 : boolean -- the first bit
    #b1 : boolean -- the second bit

    #Returns: 2 element Tuple with Boolean elements, the first element representing
    #         the subtraction a1-b1-b, and the second element contains the
    #         updated borrow for the next subtraction

    #Logic:
    #There are 8 cases to consider, b == 0 or 1, a1==b1 or a1!=b1, and a1>b1 or a1<b1 
    #XOR will separate them on the basis of a1==b1.
    #Then using if else for checking whether b == 0 or 1
    #Then using comparator for checking whether b1>a1 or not to update borrow
    
    if bool((a1 or b1) and not (a1 and b1)):
        if b:
            r1=False
            if cmp(0,0,0,b1, 0,0,0,a1):
                b=1
            else:
                b=0
        else:
            r1=True
            if cmp(0,0,0,b1, 0,0,0,a1):
                b=1
            else:
                b=0
    else:
        if b:
            r1=True
            b=1
        else:
            r1=False
            b=0
    return (r1, b)


                
#Subtraction of two 4 bit numbers
def sub4(a0,a1,a2,a3, b0,b1,b2,b3):
    #Gives the signed result of the subtraction of two 4-bit numbers

    #Parameters:
    #a0, a1, a2, a3 : boolean -- the bits of 4 bit numeral a3a2a1a0
    #b0, b1, b2, b3 : boolean -- the bits of 4 bit numeral b3b2b1b0

    #Returns: 5 element Tuple with boolean elements representing the signed result
    #         of the subtraction a3a2a1a0-b3b2b1b0 in reverse order

    #Logic: Use the sub fuction and update the borrow for next multiplication
    
    s=cmp(a0,a1,a2,a3, b0,b1,b2,b3)     #Comparing which number is bigger
    b=0                                 #Initialising the borrow digit
    
    if s:                               #If s==True, then perform a-b, else b-a
        (r0,b)=sub(a0,b0,b)             
        (r1,b)=sub(a1,b1,b)             
        (r2,b)=sub(a2,b2,b)
        (r3,b)=sub(a3,b3,b)

    else:    
        (r0,b)=sub(b0,a0,b)
        (r1,b)=sub(b1,a1,b)
        (r2,b)=sub(b2,a2,b)
        (r3,b)=sub(b3,a3,b)

    if r0 or r1 or r2 or r3:            #Extra case when all are equal, then according
        return (r0, r1, r2, r3, not s)  #to convention, the signed bit should be False
    else:
        return (r0, r1, r2, r3, s)




#COL Assignment 1 - Part 2


#8 bit adder
def add8(a, b, c):
    #Adds two 8 bit numbers and a carry bit c

    #Parameters:
    #a : 8 element Tuple -- Boolean elements representing the digits in reverse order
    #b : 8 element Tuple -- Boolean elements representing the digits in reverse order
    #c : Boolean         -- Represents the carry bit

    #Returns: 2 element Tuple -- Element 1 represent the sum a+b+c in Tuple format with
    #         with boolean elemnts representing the digits of sum in reverse order, and
    #         the second element representing the updated carry bit.

    #Logic: Use the add4 twice to sum digits in groups of 4 and update the carry bit
    
    (a0,a1,a2,a3,a4,a5,a6,a7) = a
    (b0,b1,b2,b3,b4,b5,b6,b7) = b
    
    (r0,r1,r2,r3,c) = add4(a0,a1,a2,a3,b0,b1,b2,b3,c)
    (r4,r5,r6,r7,cout) = add4(a4,a5,a6,a7,b4,b5,b6,b7,c)

    s = (r0,r1,r2,r3,r4,r5,r6,r7)   #the final sum

    return (s,cout)

        

#Multiplier
def mul4(a,b):
    #Multiply two 4 bit numbers

    #Parameters:
    #a : 4 element Tuple -- Boolean elements representing the digits in reverse order
    #b : 4 element Tuple -- Boolean elements representing the digits in reverse order

    #Returns: 8 element Tuple with boolean elements representing the digits of
    #         product a*b in reverse order

    #Logic: If b=0, return 0, Else use recursion and return a+mul4(a,b-1)
    #       For getting b-1, use sub4. For adding a and mul4(a,b-1), use add8
    
    (a0,a1,a2,a3) = a
    (b0,b1,b2,b3) = b
    
    if b0 or b1 or b2 or b3:                        #if any one is non zero
        
        a_new=(a0,a1,a2,a3,0,0,0,0)                 #Make 'a' to be 8 bit for using add8

        (b0,b1,b2,b3,k) = sub4(b0,b1,b2,b3,1,0,0,0) #subtracting 1 from b
        
        m = mul4(a,(b0,b1,b2,b3))                   #Recursion
        
        (r,c)=add8(a_new,m,0)
        
        return r
    else:
        return (False,False,False,False,False,False,False,False)
