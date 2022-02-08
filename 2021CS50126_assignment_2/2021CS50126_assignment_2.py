###COL Assignment-2###
#--------------------#


#The following functions are taken from assignment 1.

#Full Adder -- Helper for add4
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
    
    ab=(a or b) and not (a and b)
    
    return (bool((ab or c) and not (ab and c)),bool((a and b) or (a and c) or (b and c)))




#4-bit adder -- Helper for add8
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




#8 bit adder -- Helper for mul4
def add8(a, b, c):
    #Adds two 8 bit numbers and a carry bit c

    #Parameters:
    #a : 8 element Tuple -- Boolean elements representing the digits in reverse order
    #b : 8 element Tuple -- Boolean elements representing the digits in reverse order
    #c : Boolean         -- Represents the carry bit

    #Returns: Tuple representing the sum a+b+c in Tuple format with boolean elements
    #         representing the digits of sum in reverse order.

    #Logic: Use the add4 twice to sum digits in groups of 4 and update the carry bit
    
    (a0,a1,a2,a3,a4,a5,a6,a7) = a
    (b0,b1,b2,b3,b4,b5,b6,b7) = b
    
    (r0,r1,r2,r3,c) = add4(a0,a1,a2,a3,b0,b1,b2,b3,c)
    (r4,r5,r6,r7,cout) = add4(a4,a5,a6,a7,b4,b5,b6,b7,c)

    s = (r0,r1,r2,r3,r4,r5,r6,r7)   #the final sum

    return (s,cout)

#-----------------------------------------------------------------------------------#


#Assignment-2 Functions


#Helper for mul4
def mult(a,b):
    #Multiplies a tuple with a bit

    #Parameters:
    #a : 4 element Tuple -- Boolean elements representing the digits in reverse order
    #b : Boolean         -- A single bit

    #Returns: 4 element Tuple consisting of the product a*b, with boolean elements
    #         representing the product in reverse order.

    #Logic: If b=0, return 0, else b would be 1, so return a.
    
    if b:
        return a
    else:
        return (False,False,False,False)


    
#Q3
#4 bit multiplier
def mul4(a,b):
    #Multiplies a tuple with another tuple.

    #Parameters:
    #a : 4 element Tuple -- Boolean elements representing the digits in reverse order
    #b : 4 element Tuple -- Boolean elements representing the digits in reverse order

    #Returns: 8 element Tuple consisting of the product a*b, with boolean elements
    #         representing the product in reverse order.

    (a0,a1,a2,a3) = a
    (b0,b1,b2,b3) = b
    ans = (False,False,False,False,False,False,False,False)

    (p01,p02,p03,p04) = mult(a,b0)  #multiplying and storing the single bit products
    (p11,p12,p13,p14) = mult(a,b1)
    (p21,p22,p23,p24) = mult(a,b2)
    (p31,p32,p33,p34) = mult(a,b3)

    (ans, cout) = add8(ans,(p01,p02,p03,p04,False,False,False,False),False) #similar to using join()
    (ans, cout) = add8(ans,(False,p11,p12,p13,p14,False,False,False),False) #as defined in the algorithm,
    (ans, cout) = add8(ans,(False,False,p21,p22,p23,p24,False,False),False) #adding the required number
    (ans, cout) = add8(ans,(False,False,False,p31,p32,p33,p34,False),False) #of zeroes at end, then
                                                                            #summing up everything
    
    return ans

                        #-----------------#


#4 bit iterative multiplier helper
def mul4ihelper(a,b,result,index):
    #Multiplies a tuple with another tuple using iterative approach.

    #Parameters:
    #a : 4 element Tuple -- Boolean elements representing the digits in reverse order
    #b : 4 element Tuple -- Boolean elements representing the digits in reverse order
    #result : 8 element Tuple -- Boolean elements representing the digits in reverse order
    #index : integer -- Represents how many times recursion has happened.

    #Returns: 8 element Tuple consisting of the product a*b, with boolean elements
    #         representing the product in reverse order.

    
    if index==3:        #that is, have checked all digits of b
        return result
        
    else:
        (a0,a1,a2,a3)=a
        (b0,b1,b2,b3)=b
        
        (r0,r1,r2,r3,r4,r5,r6,r7)=result
        
        index+=1                                #increment in index

        result=(False,r0,r1,r2,r3,r4,r5,r6)     #used join(result,0,1) as in algorithm

        if index==0 and b3:
            (result,c)=add8(result,(a0,a1,a2,a3,False,False,False,False),False)
            
        if index==1 and b2: #b3 has been checked and is gone due to lower()
            (result,c)=add8(result,(a0,a1,a2,a3,False,False,False,False),False)
            
        if index==2 and b1: #b3 and b2 has been checked and is gone due to lower()
            (result,c)=add8(result,(a0,a1,a2,a3,False,False,False,False),False)
            
        if index==3 and b0: #b3, b2 and b1 has been checked and is gone due to lower()
            (result,c)=add8(result,(a0,a1,a2,a3,False,False,False,False),False)
        
        return mul4ihelper(a,b,result,index)



#Q5
#4 bit iterative multiplier
def mul4i(a,b):
    #Multiplies a tuple with another tuple using iterative approach.

    #Parameters:
    #a : 4 element Tuple -- Boolean elements representing the digits in reverse order
    #b : 4 element Tuple -- Boolean elements representing the digits in reverse order

    #Returns: 8 element Tuple consisting of the product a*b, with boolean elements
    #         representing the product in reverse order.
    
    return mul4ihelper(a,b,(False,False,False,False,False,False,False,False),-1)

                            #---------------------#
