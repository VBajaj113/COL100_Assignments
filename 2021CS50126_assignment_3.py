#COL Assignment 3
#-----------------#
#Taylor Series Expansion
#------------------------#

import math         #For ques 2
pi=math.pi          #For input in cosine function

#Question 1

def expn(x,n):
    #The approximation of e^x upto n terms of the taylor series expansion

    #Input Parameters:
    #x (any real number): float -- The power to which e is raised to
    #n >= 1: integer -- The number of terms to be considered for approximation in the taylor series

    #Returns: float -- The approximation of e^x upto n terms of the taylor series
    #OUTPUT: 1 + x + x^2/2! +...+ x^(n-1)/(n-1)!
    
    #Initialisation:                                    #O(1) time
    i=1             #the counter from 1 to n terms
    ans=1           #ans for n=1 case
    prev=1          #the ith term of the taylor series

    #Invariant1: prev = the ith term of the series = x^(i-1)/(i-1)!
    #Invariant2: ans = sum of first i terms of the series
    
    #Checking before loop:
    #prev == 1 == x^0/0! == x^(i-1)/(i-1)! when i == 1
    #ans == 1 == sum of 1st term == sum of i terms

    while i<n:          #Termination: n-i decreases to 0
        
        #prev == x^(i-1)/(i-1)!
        prev*=x/i       #O(1) time as always a constant number of operations are performed
        #prev == x^i/i!

        #ans == sum of i terms
        ans+=prev       #O(1) time as always a constant number of operations are performed
        #ans == sum of i terms + (i+1)th term == sum of i+1 terms

        i+=1            #O(1) time as always a constant number of operations are performed

        #Checking Invariant:
        #Invariant1: prev == x^(i-1)/(i-1)!
        #Invariant2: ans == sum of i terms of the series
        #==> Invariant is maintained

    #Time Complexity:
    #For each iteration, it takes 3*O(1) = O(1) time. Therefore for n-1 iterations, it will take
    #(n-1)*O(1) = O(n) time.Adding the time for initialisation, O(n)+O(1) = O(n)
    #So, the time compexity of the algorithm is O(n)

    #Exit condition when n-i == 0 ==> n == i
    #So, Invariant1 implies prev == x^(n-1)/(n-1)!
    #Invariant2 implies ans == sum of n terms of the series

    return ans


def cosine(x,n):
    #The approximation of cos(x) upto n terms of the taylor series expansion

    #Input Parameters:
    #x (angle in radians): float -- The cosine of which is to be found
    #n >= 1: integer -- The number of terms to be considered for approximation in the taylor series

    #Returns: float -- The approximation of cos(x) upto n terms of the taylor series
    #OUTPUT: 1 - x^2/2! + x^4/4! + ... + (-1)^(n+1) x^(2n-2)/(2n-2)!

    #Initialisation:                                #O(1) time for initialisation
    i=1             #the counter from 1 to n terms
    ans=1           #ans for n=1 case
    prev=1          #the ith term of the taylor series
    
    #Invariant1: prev = the ith term of the series = -1^(i+1) x^(2i-2)/(2i-2)!
    #Invariant2: ans = sum of first i terms of the series

    #Checking before loop:
    #prev == 1 == (-1)^2 x^0/0! == (-1)^(i+1) x^(2i-2)/(2i-2)! when i == 1
    #ans == sum of 1st term == 1

    while i<n:            #Termination: n-i decreases to 0

        #prev == (-1)^(i+1) x^(2i-2)/(2i-2)!
        prev*=-x*x/(2*i*(2*i-1))    #O(1) time as always a constant number of operations are performed
        #prev == (-1)^(i+2) x^(2i)/(2i)!

        #ans == sum of i terms
        ans+=prev                   #O(1) time as always a constant number of operations are performed
        #ans == sum of i terms + (i+1)th term == sum of i+1 terms

        i+=1                        #O(1) time as always a constant number of operations are performed

        #Checking Invariant:
        #Invariant1: prev == -1^(i+1) x^(2i-2)/(2i-2)!
        #Invariant2: ans == sum of i terms of the series
        #==> Invariant is maintained
    
    #Time Complexity:
    #For each iteration, it takes 3*O(1) = O(1) time. Therefore for n-1 iterations, it will take
    #(n-1)*O(1) = O(n) time. Adding the time for initialisation, O(n)+O(1) = O(n)
    #So, the time compexity of the algorithm is O(n)

    #Exit condition when n-i == 0 ==> n==i
    #So, Invairant1 implies prev == -1^(n+1) x^(2n-2)/(2n-2)!
    #Invariant2 implies ans == sum of n terms of the series

    return ans


def inverse(x,n):
    #The approximation of 1/(1-x) upto n terms of the taylor series expansion

    #Input Parameters:
    #x (any real number: -1 < x < 1): float -- The value of x to be used in the approximation
    #n >= 1: integer -- The number of terms to be considered for approximation in the taylor series

    #Returns: float -- The approximation of 1/(1-x) upto n terms of the taylor series
    #OUTPUT: 1 + x + x^2 + ... + x^(n-1)

    #Initialisation:                                #O(1) time for initialisation
    i=1             #the counter from 1 to n terms
    ans=1           #ans for n=1 case
    prev=1          #the ith term of the taylor series

    #Invariant1: prev = the ith term of the series = x^(i-1)
    #Invariant2: ans = sum of first i terms of the series

    #Checking before loop:
    #prev == 1 == x^0 == x^(i-1) when i==1
    #ans == sum of 1st term == 1

    while i<n:          #Termination: n-i decreases to 0

        #prev == x^(i-1)
        prev*=x         #O(1) time as always a constant number of operations are performed
        #prev == x^i

        #ans == sum of i terms
        ans+=prev       #O(1) time as always a constant number of operations are performed
        #ans == sum of i terms + (i+1)th term == sum of i+1 terms

        i+=1            #O(1) time as always a constant number of operations are performed

        #Checking Invariant:
        #Invariant1: prev == x^(i-1)
        #Invariant2: ans == sum of i terms of the series
        #==> Invariant is maintained
    
    #Time Complexity:
    #For each iteration, it takes 3*O(1) = O(1) time. Therefore for n-1 iterations, it will take
    #(n-1)*O(1) = O(n) time. Adding the time for initialisation, O(n)+O(1) = O(n)
    #So, the time compexity of the algorithm is O(n)

    #Exit condition when n-i == 0 ==> n==i
    #So, Invairant1 implies prev == x^(n-1)
    #Invariant2 implies ans == sum of n terms of the series

    return ans


def natural_log(x,n):
    #The approximation of ln(1+x) upto n terms of the taylor series expansion

    #Input Parameters:
    #x (any real number: -1 < x <= 1): float -- The value of which log is to be found
    #n >= 1: integer -- The number of terms to be considered for approximation in the taylor series

    #Returns: float -- The approximation of ln(1+x) upto n terms of the taylor series
    #OUTPUT: x - x^2/2 + x^3/3 - ... + (-1)^(n+1) x^n/n

    #Initialisation:                                #O(1) time for initialisation
    i=1             #the counter from 1 to n terms
    ans=x           #ans for n=1 case
    prev=x          #the ith term of the taylor series

    #Invariant1: prev = the ith term of the series = (-1)^(i+1) x^i/i
    #Invariant2: ans = sum of first i terms of the series

    #Checking before loop:
    #prev == x == (-1)^2 x^1/1 == (-1)^(i+1) x^i/i when i==1
    #ans == sum of 1st term == x

    while i<n:              #Termination: n-i decreases to 0

        #prev == (-1)^(i+1) x^i/i
        prev*=-x*i/(i+1)            #O(1) time as always a constant number of operations are performed
        #prev == -1^(i+2) x^(i+1)/(i+1)

        #ans == sum of i terms
        ans+=prev                   #O(1) time as always a constant number of operations are performed
        #ans == sum of i terms + (i+1)th term == sum of i+1 terms

        i+=1                        #O(1) time as always a constant number of operations are performed

        #Checking Invariant:
        #Invariant1: prev == (-1)^(i+1) x^i/i
        #Invariant2: ans == sum of i terms of the series
        #==> Invariant is maintained

    #Time Complexity:
    #For each iteration, it takes 3*O(1) = O(1) time. Therefore for n-1 iterations, it will take
    #(n-1)*O(1) = O(n) time. Adding the time for initialisation, O(n)+O(1) = O(n)
    #So, the time compexity of the algorithm is O(n)

    #Exit condition when n-i == 0 ==> n==i
    #So, Invairant1 implies prev == (-1)^(n+1) x^n/n
    #Invariant2 implies ans == sum of n terms of the series

    return ans


def tan_inv(x,n):
    #The approximation of arctan(x) upto n terms of the taylor series expansion

    #Input Parameters:
    #x (any real number): float -- The number whose arctan is to be found
    #n >= 1: integer -- The number of terms to be considered for approximation in the taylor series

    #Returns: float -- The approximation of arctan(x) upto n terms of the taylor series
    #OUTPUT: x - x^3/3 + x^5/5 - ... + (-1)^(n+1) x^(2n-1)/(2n-1)

    #Initialisation:                                #O(1) time for initialisation
    i=1             #the counter from 1 to n terms
    ans=x           #ans for n=1 case
    prev=x          #the ith term of the taylor series

    #Invariant1: prev = the ith term of the series = (-1)^(i+1) x^(2i-1)/(2i-1)
    #Invariant2: ans = sum of first i terms of the series

    #Checking before loop:
    #prev == x == (-1)^2 x^(2*1-1)/(2*1-1) == (-1)^(i+1) x^(2i-1)/(2i-1) when i == 1
    #ans == sum of 1st term == x

    while i<n:              #Termination: n-i decreases to 0

        #prev == (-1)^(i+1) x^(2i-1)/(2i-1)
        prev*=-x*x*(2*i-1)/(2*i+1)      #O(1) time as always a constant number of operations are performed      
        #prev == (-1)^(i+2) x^(2i+1)/(2i+1)

        #ans == sum of i terms
        ans+=prev                       #O(1) time as always a constant number of operations are performed
        #ans == sum of i terms + (i+1)th term == sum of i+1 terms

        i+=1                            #O(1) time as always a constant number of operations are performed

        #Checking Invariant:
        #Invariant1: prev == (-1)^(i+1) x^(2i-1)/(2i-1)
        #Invariant2: ans == sum of i terms of the series
        #==> Invariant is maintained

    #Time Complexity:
    #For each iteration, it takes 3*O(1) = O(1) time. Therefore for n-1 iterations, it will take
    #(n-1)*O(1) = O(n) time. Adding the time for initialisation, O(n)+O(1) = O(n)
    #So, the time compexity of the algorithm is O(n)

    #Exit condition when n-i == 0 ==> n==i
    #So, Invairant1 implies prev == (-1)^(n+1)x^(2n-1)/(2n-1)
    #Invariant2 implies ans == sum of n terms of the series

    return ans


#----------------------------------------------------------------------------------------------------------#

#Question 2

#Entry Number = 2021CS50126
#Remainder = 2

def absolute(x):
    #Gives the absolute value of a number

    #Input Parameters:
    #x: float -- any real number

    #Returns: float -- the absolute value of x
    #OUTPUT: |x|

    if x>=0:            #O(1) time for checking
        return x

    else:
        return -x
    #Therefore the time complexity of this algorithm is O(1)


def f(x):           # f: R --> R
    #function for which root has to be found

    #Input Parameter: 
    #x: float -- The value of which the function has to be found

    #Input Constraints:
    #x !=1 as the domain does not contain 1.

    #Returns: the value of sin(x)+1/(1-x)

    return math.sin(x)+1/(1-x)      #O(1) time as a constant number of operations are performed


def bisect(a,b,epsilon):
    #Root finder for sin(x) + 1/(1-x) via bisection method

    #Input Parameters:
    #a (any real number): float -- The lower limit for the range of root 
    #b (any real number): float -- The upper limit for the range of root
    #epsilon (any real number): float -- The tolerance on output

    #Input Constraints:
    #a<b
    #f(a)*f(b)<0
    #Found == True ==> |f(Value)| <= epsilon
    #epsilon > 0 and epsilon ~ 0

    #Returns: A tuple of 3 elements
    #Found: Boolean -- denotes if there is a root of the function in the given interval
    #Value: Float -- the root of the function in the given interval with tolerance of epsilon, if it exists
    #IterList: List with float elements -- denotes the sequence of approximate results as the iteration converges
    #                                      towards the root

    #Initialisation:    #O(1) time for initialisation
    counter = 0         #To keep track of how many times the loop ran
    IterList=[]         #Initial list with no approximation
    Found=False         #Initially false as no root is found
    Value = a           #Initially givinig a value to avoid giving a error

    #Invariants:
    #Invariant1: IterList == Contains counter number of approximations
    #Invariant2: range == (b-a)/2^(counter)

    if f(b)>=0:                                 #O(1) time for checking

        while (not Found) and (a<b):            #Termination: range decreases till (b-a)/2^counter < tol
            
            mid=(a+b)/2                         #bisect the interval                    #O(1) Time for assigning value
            temp=f(mid)                         #Storing the value of f(mid) in temp    #O(1) Time for assigning value

            if mid==1:                          #if mid==1, it is an asymptote of f. So will give an error  #O(1) Time for checking
                return(Found,mid,IterList)      #So, return false and stop the execution of the function
            
            elif absolute(temp)<=epsilon:            #Answer is found       #O(1) Time for checking
                Found=True                                             #O(1) Time for changing value
                Value=mid                                              #O(1) Time for changing value
            
            elif temp>0:                        #Move the boundary of interval laftwards    #O(1) Time for checking
                b=mid                                                                       #O(1) Time for changing value

            else:                               #Move the boundary of the interval rightwards
                a=mid                           #O(1) Time for changing value
            
            IterList.append(mid)                #Appending the next apprpoximation          #O(1) Time for appending
            counter+=1                                                                      #O(1) Time for updating
            #Loop Exit: Either (found == True) or (a >= b) or mid==1
    
    else:
        
        while (not Found) and (a<b):            #Termination: b-a decreases
            
            mid=(a+b)/2                         #bisect the interval                    #O(1) Time for assigning value
            temp=f(mid)                         #Storing the value of f(mid) in temp    #O(1) Time for assigning value

            if mid==1:                          #if mid==1, it is an asymptote of f. So will give an error  #O(1) Time for checking
                return(Found,mid,IterList)      #So, return false and stop the execution of the function
            
            elif absolute(temp)<=epsilon:            #Answer is found       #O(1) Time for checking
                Found=True                                             #O(1) Time for changing value
                Value=mid                                              #O(1) Time for changing value
            
            elif temp>0:                        #Move the boundary of interval laftwards    #O(1) Time for checking
                a=mid                                                                       #O(1) Time for changing value

            else:                               #Move the boundary of the interval rightwards
                b=mid                           #O(1) Time for changing value
            
            IterList.append(mid)                #Appending the next apprpoximation          #O(1) Time for appending
            counter+=1                                                                      #O(1) Time for updating
            #Loop Exit: Either (found == True) or (a >= b) or mid==1

    #Time Complexity:
    #At every iteration, the value of rannge in which we have to find a root reduces to half. 
    #As the width of the bisected interaval is always greater than or equal to threshold 'tol', 
    #therefore whenever k < tol, the loop would stop. As k halves everytime, so:
    #k/2^z < tol implies the iteration runs z times.
    #So O(z) is the time complexity.
    #Let z be a natural number such that 2^(z-1) < (b-a)/tol <= 2^z. Therefore:
    #z-1 < log_2 ((b-a)/epsilon) <= z. Therefore:
    #O(z) < O(log((b-a)/tol)) <= O(z)
    #So, Time complexity is O(log((b-a)/tol)).

    return(Found,Value,IterList)


#-----------------------------------------------------------------------------------------------------------#

#Question 3

def fac(n):
    #Finds the factorial of the number n

    #Input Parameters:
    #n >= 0 : integer -- the factorial of whose is to be found

    #Returns: integer -- n!, the factorial of n

    #Initialisation:        #O(1) time for initialisation
    i=0             #the counter variable
    ans=1           #ans for n=0 case

    #Invariant: ans = i!

    #Checking before the loop:
    #ans = 1 = 0! = i!

    while i<n:          #Termination: n-i decreases to 0
        
        #i = i
        i+=1            #O(1) time for updating value
        #i = i+1

        #ans = (i-1)!
        ans*=i          #O(1) time for a single multiplication
        #ans = i!

        #Checking after the loop:
        #ans = i! ==> Invariant is maintained
    
    #Exit Condition when i==n 
    #Therefore the invariant implies ans = i! = n!

    #Time Complexty:
    #For one iteration of loop, it takes 2*O(1) = O(1) time. As the loop runs n times, therefore
    #time complexity is n*O(1) = O(n) time. Adding time for initialisation, O(n)+O(1) = O(n).
    #Therefore, time complexity is O(n).

    return ans


def expn_coeff(n):
    #Returns the coefficient of nth power of x in the taylor series of e^x

    #Input Parameters:
    #n >= 0 : integer -- the power of x

    #Returns: float -- the coefficient of nth power of x in the taylor series of e^x
    #OUTPUT: 1/n!

    ans = 1/fac(n)          #As fac(n) has O(n) time complexity and a single division has O(1) time complexity,
                            #Therefore overall time complexity is O(n)+O(1) = O(n)
    return ans
                            

def cosine_coeff(n):
    #Returns the coefficient of nth power of x in the taylor series of cosine(x)

    #Input Parameters:
    #n >= 0 : integer -- the power of x

    #Returns: float -- the coefficient of nth power of x in the taylor series of cosine(x)
    #OUTPUT: (-1)^(n/2)/n! or 0.0

    ans = 1/fac(n)          #As fac(n) has O(n) time complexity and a single division has O(1) time complexity,
                            #Therefore overall time complexity for this step is O(n) + O(1) = O(n)

    if n%4==0:              #O(1) time for checking
        return ans

    elif n%4==2:            #O(1) time for checking
        return -ans
    
    else:
        return 0.0
    #Therefore, overall time complexity is O(n)+O(1)+O(1) = O(n)


def inverse_coeff(n):
    #Returns the coefficient of nth power of x in the taylor series of 1/(1-x)

    #Input Parameters:
    #n >= 0 : integer -- the power of x

    #Returns: float -- the coefficient of nth power of x in the taylor series of 1/(1-x)
    #OUTPUT: 1.0

    return 1.00     #O(1) time complexity overall


def natural_log_coeff(n):
    #Returns the coefficient of nth power of x in the taylor series of log(x)

    #Input Parameters:
    #n >= 0 : integer -- the power of x

    #Returns: float -- the coefficient of nth power of x in the taylor series of log(x)
    #OUTPUT: (-1)^(n+1)/n or 0.0
    
    if n==0:                #O(1) time for checking
        return 0.0

    ans = 1/n               #O(1) time complexity

    if n%2==0:              #O(1) time for checking
        return -ans

    else:
        return ans
    #Therefore the time complexity for this function is O(1)+O(1)+O(1) = O(1)


def tan_inv_coeff(n):
    #Returns the coefficient of nth power of x in the taylor series of arctan(x)

    #Input Parameters:
    #n >= 0 : integer -- the power of x

    #Returns: float -- the coefficient of nth power of x in the taylor series of arctan(x)
    #OUTPUT: (-1)^((n-1)/2)/n or 0.0

    if n%2==0:              #O(1) time for checking
        return 0.0
    
    ans = 1/n               #O(1) time for initialising

    if n%4==1:              #O(1) time for checking
        return ans

    else:
        return -ans
    #Therefore the time complexity for this function is O(1)+O(1)+O(1) = O(1)


#------------------------------------------------------------------------------------------------------------#

#Question 4

def power(x,n):
    #Gives the value of x^n

    #Input Parameters:
    #x: float -- the number whose power is to be raised
    #n >= 0 : integer -- the power of x

    #Returns: float -- x^n

    #Initialisation:                                #O(1) time for initialisation
    i=0                 #Counter
    ans=1               #The value of x^0

    #Invariant: ans = x^i

    #Checking before the loop:
    #ans = 1 = x^0 = x^i

    while i<n:          #Termination: n-i reduces to 0

        #ans = x^i
        ans*=x          #O(1) time complexity as it has a constant number of operations
        #ans = x^(i+1)
        
        i+=1            #O(1) time complexity as it has a constant number of operations

        #Checking after the loop:
        #ans = x^i ==> invariant is maintained
    
    #Time Complexity:
    #For each iteration, it takes 2*O(1) = O(1) time. Therefore for n iterations, it will take
    #n*O(1) = O(n) time. Adding the time for initialisation, O(n)+O(1)=O(n).
    #So, the time compexity of the algorithm is O(n)

    #Exit condition when n-i == 0 ==> n==i
    #So, invariant implies ans = x^i = x^n

    return ans


def expn_t(x,n):
    #Gives the sum of taylor series of e^x upto the nth power of x

    #Input Parameters:
    #x: float -- the power of e
    #n >= 0: integer -- the power of x upto which the taylor series is to be evaluated

    #Returns: float -- the value of taylor series approximation of e^x upto x^n term
    #OUTPUT: 1 + x + x^2/2! +...+ x^n/n!

    #Initialisation:                                #O(1) time for initialisation
    ans = 1             #Initialisation of answer for n=1
    i = 0               #Counter

    #Invariant:
    #ans = sum of taylor series series expansion of e^x upto x^i term

    #Checking before loop:
    #ans == 1 == sum upto x^0 term == sum upto x^i term

    while i<n:         #Termination: n-i decreaases to 0
        
        i+=1                            #O(1) time complexity

        #ans = sum upto x^(i-1) term
        ans+= expn_coeff(i)*power(x,i)  #O(i)+O(i)+2*O(1) = O(i) time complexity
        #ans = sum upto x^i term

        #Checking Invariant:
        #ans == sum of taylor series of e^x upto x^i term
        #==> Invariant is maintained
    
    #Time Complexity:
    #For each iteration, it takes O(i)+O(1) = O(i) time. Therefore for n iterations, it will take
    #summation (O(i)) from i=1 to i=n.
    #So, Time complexity is O(1) + O(2) + O(3) + ... + O(n) = O(n*n)
    #As initialisation takes O(1) time, the time compexity of the algorithm is O(n*n) + O(1).
    #Therefore the time complexity of the algorithm is O(n*n)

    #Exit condition when n-i == 0 ==> n==i
    #So, invariant implies ans == sum of taylor series series of e^x upto x^n term

    return ans


def cosine_t(x,n):
    #The approximation of cos(x) upto x^n term of the taylor series expansion

    #Input Parameters:
    #x (angle in radians): float -- The cosine of which is to be found
    #n >= 0: integer -- the power of x upto which the taylor series is to be evaluated

    #Returns: float -- the value of taylor series approximation of cosine(x) upto x^n term
    #OUTPUT: 1 - x^2/2! + x^4/4! + ... + (-1)^(n/2) x^n/n!

    #Initialisation:                                #O(1) time for initialisation
    ans = 1         #The answer for n = 0 case
    i = 0           #counter

    #Invariant:
    #ans = sum of taylor series series expansion of cosine(x) upto x^i term

    #Checking before loop:
    #ans == 1 == sum upto x^0 term == sum upto x^i term

    while i<n:          #Termination: n-i decreaases to 0

        i+=1                                #O(1) time complexity
        
        #ans = sum upto x^(i-1) term
        ans+= cosine_coeff(i)*power(x,i)    #O(i)+O(i)+2*O(1) = O(i) time complexity
        #ans = sum upto x^i term

        #Checking Invariant:
        #ans == sum of taylor series of cosine(x) upto x^i term
        #==> Invariant is maintained
    
    #Time Complexity:
    #For each iteration, it takes O(i)+O(1) = O(i) time. Therefore for n iterations, it will take
    #summation (O(i)) from i=1 to i=n.
    #So, Time complexity is O(1) + O(2) + O(3) + ... + O(n) = O(n*n)
    #As initialisation takes O(1) time, the time compexity of the algorithm is O(n*n) + O(1).
    #Therefore the time complexity of the algorithm is O(n*n)

    #Exit condition when n-i == 0 ==> n==i
    #So, invariant implies ans == sum of taylor series series of cosine(x) upto x^n term

    return ans


def inverse_t(x,n):
    #The approximation of 1/(1-x) upto x^n term of the taylor series expansion

    #Input Parameters:
    #x (any real number: -1 < x < 1): float -- The value of x to be used in the approximation
    #n >= 0: integer -- the power of x upto which the taylor series is to be evaluated

    #Returns: float -- the value of taylor series approximation of 1/(1-x) upto x^n term
    #OUTPUT: 1 + x + x^2 + ... + x^n

    #Initialisation:                                #O(1) time for initialisation
    ans = 1         #The answer for n = 0 case
    i = 0           #counter

    #Invariant:
    #ans = sum of taylor series series expansion of 1/(1-x) upto x^i term

    #Checking before loop:
    #ans == 1 == sum upto x^0 term == sum upto x^i term

    while i<n:          #Termination: n-i decreaases to 0
        
        i+=1                                    #O(1) time complexity
        
        #ans = sum upto x^(i-1) term
        ans+= inverse_coeff(i)*power(x,i)       #O(1)+O(i)+2*O(1) = O(i) time complexity
        #ans = sum upto x^i term

        #Checking Invariant:
        #ans == sum of taylor series of 1/(1-x) upto x^i term
        #==> Invariant is maintained
    
    #Time Complexity:
    #For each iteration, it takes O(i)+O(1) = O(i) time. Therefore for n iterations, it will take
    #summation (O(i)) from i=1 to i=n.
    #So, Time complexity is O(1) + O(2) + O(3) + ... + O(n) = O(n*n)
    #As initialisation takes O(1) time, the time compexity of the algorithm is O(n*n) + O(1).
    #Therefore the time complexity of the algorithm is O(n*n)

    #Exit condition when n-i == 0 ==> n==i
    #So, invariant implies ans == sum of taylor series series of 1/(1-x) upto x^n term

    return ans


def natural_log_t(x,n):
    #The approximation of log(x) upto x^n term of the taylor series expansion

    #Input Parameters:
    #x (any real number: -1 < x <= 1): float -- The value for which log(1+x) is to be found
    #n >= 0: integer -- The number of terms to be considered for approximation in the taylor series

    #Returns: float -- the value of taylor series approximation of log(1+x) upto x^n term
    #OUTPUT: x - x^2/2! + x^3/3! - ... + (-1)^(n+1)x^n/n!

    #Initialisation:                                #O(1) time for initialisation
    ans = 0         #The answer for n = 0 case
    i = 0           #counter

    #Invariant:
    #ans = sum of taylor series series expansion of log(1+x) upto x^i term

    #Checking before loop:
    #ans == 0 == sum upto x^0 term == sum upto x^i term

    while i<n:          #Termination: n-i decreaases to 0

        i+=1                                        #O(1) time complexity
        
        #ans = sum upto x^(i-1) term
        ans+= natural_log_coeff(i)*power(x,i)       #O(1)+O(i)+2*O(1) = O(i) time complexity
        #ans = sum upto x^i term
        
        #Checking Invariant:
        #ans == sum of taylor series of log(x) upto x^i term
        #==> Invariant is maintained
    
    #Time Complexity:
    #For each iteration, it takes O(i)+O(1) = O(i) time. Therefore for n iterations, it will take
    #summation (O(i)) from i=1 to i=n.
    #So, Time complexity is O(1) + O(2) + O(3) + ... + O(n) = O(n*n)
    #As initialisation takes O(1) time, the time compexity of the algorithm is O(n*n) + O(1).
    #Therefore the time complexity of the algorithm is O(n*n)

    #Exit condition when n-i == 0 ==> n==i
    #So, invariant implies ans == sum of taylor series series of log(1+x) upto x^n term

    return ans


def tan_inv_t(x,n):
    #The approximation of aractan(x) upto x^n term of the taylor series expansion

    #Input Parameters:
    #x (any real number): float -- The number whose arctan is to be found
    #n >= 0: integer -- The number of terms to be considered for approximation in the taylor series

    #Returns: float -- the value of taylor series approximation of arctan(x) upto x^n term
    #OUTPUT: x - x^3/3 + x^5/5 - ... + (-1)^((n-1)/2)x^n/n

    #Initialisation:                                #O(1) time for initialisation
    ans = 0         #The answer for n = 0 case
    i = 0           #counter

    #Invariant:
    #ans = sum of taylor series series expansion of arctan(x) upto x^i term

    #Checking before loop:
    #ans == 0 == sum upto x^0 term == sum upto x^i term

    while i<n:          #Termination: n-i decreaases to 0

        i+=1                                        #O(1) time complexity
        
        #ans = sum upto x^(i-1) term
        ans+= tan_inv_coeff(i)*power(x,i)           #O(1)+O(i)+2*O(1) = O(i) time complexity
        #ans = sum upto x^i term

        #Checking Invariant:
        #ans == sum of taylor series of arctan(x) upto x^i term
        #==> Invariant is maintained
    
    #Time Complexity:
    #For each iteration, it takes O(i)+O(1) = O(i) time. Therefore for n iterations, it will take
    #summation (O(i)) from i=1 to i=n.
    #So, Time complexity is O(1) + O(2) + O(3) + ... + O(n) = O(n*n)
    #As initialisation takes O(1) time, the time compexity of the algorithm is O(n*n) + O(1).
    #Therefore the time complexity of the algorithm is O(n*n)

    #Exit condition when n-i == 0 ==> n==i
    #So, invariant implies ans == sum of taylor series series of arctan(x) upto x^n term

    return ans


#-------------------------------------------------------------------------------------------------------------#

#Question 5

#2021CS50126
#Remainder = 2

#f(x) = 1/(1-x)         g(x) = e^(-x)

def add_coeff(n):
    #Gives the coefficient of x^n of (f+g)(x) = f(x)+g(x)

    #Input Parameters:
    #n >= 0: integer -- the power of x whose coefficient is to be found

    #Returns: float -- the coefficient of x^n in (f+g)(x)
    #OUTPUT: 1 + (-1)^n/n!

    if n%2==0:                                   #O(1) time to check
        return expn_coeff(n)+inverse_coeff(n)    #Time Complexity = O(n)+O(1) = O(n)

    else:
        return -expn_coeff(n)+inverse_coeff(n)   #Time Complexity = O(n)+O(1) = O(n)
    #Therefore overall time complexity = O(n)


def mul_coeff(n):
    #Gives the coefficient of x^n of (f*g)(x) = f(x)*g(x)

    #Input Parameters:
    #n >= 0: integer -- the power of x whose coefficient is to be found

    #Returns: float -- the coefficient of x^n in (f*g)(x)
    #OUTPUT: sum of x^n term for (x^j of f(x))*(x^(n-j) of g(x)) for 0 <= j <= n

    #Initialisation:                                #O(1) time for initialisation
    i = 0           #counter
    ans = 0         #Initialisation of answer

    #Invariant:
    #ans = sum of x^n term for (x^j of f(x))*(x^(n-j) of g(x)) for 0 <= j < i

    while i<=n:         #Terminates as n+1-i reduces to 0

        if i%2==0:

            #ans = sum of x^n term for (x^j of f(x))*(x^(n-j) of g(x)) for 0 <= j < i
            ans+=(expn_coeff(i)*inverse_coeff(n-i))         #O(i)+O(1)+2*O(1) = O(i) time complexity
            #ans = sum of x^n term for (x^j of f(x))*(x^(n-j) of g(x)) for 0 <= j < i+1

        else:

            #ans = sum of x^n term for (x^j of f(x))*(x^(n-j) of g(x)) for 0 <= j < i
            ans+=(-expn_coeff(i)*inverse_coeff(n-i))        #O(i)+O(1)+2*O(1) = O(i) time complexity
            #ans = sum of x^n term for (x^j of f(x))*(x^(n-j) of g(x)) for 0 <= j < i+1

        i+=1            #O(1) time complexity

        #Checking invariant after the loop:
        #ans = sum of x^n term for (x^j of f(x))*(x^(n-j) of g(x)) for 0 <= j < i
        #==>Invariant is maintained
    
    #Time Complexity:
    #For each iteration, it takes O(i)+O(1) = O(i) time. Therefore for n+1 iterations, it will take
    #O(0)+O(1)+O(2)+...+O(n) time = O(n*n) time.
    #So, the time compexity of the algorithm is O(n*n)

    #Exit condition when n+1-i == 0 ==> n+1==i
    #So, invariant implies ans == sum of x^n term for (x^j of f(x))*(x^(n-j) of g(x)) for 0 <= j <= n

    return ans


def diff_coeff(n):
    #Gives the coefficient of x^n of d(f(x))/dx

    #Input Parameters:
    #n >= 0: integer -- the power of x whose coefficient is to be found

    #Returns: float -- the coefficient of x^n of d(f(x))/dx

    #As f(x) = 1/(1-x) = 1 + x + x^2 +...+ x^n +...
    #d(f(x))/dx = 1 + 2x + 3x^2 +...+ nx^(n-1) +...
    #So, OUTPUT = n+1

    return (n+1)*inverse_coeff(n+1)            #Time Complexity = O(1)


#-------------------------------------------------------------------------------------------------------------#

#Question 6

#2021CS50126
#Remainder = 2

#cosx/(1-x)

def limit_diff(x,epsilon):
    #Gives the first order differential of (cos(x)/(1-x)) using the first principles

    #Input Parameters:
    #-1 < x < 1: float -- the value at which derivative is to be found
    #epsilon: float -- the value of h in the first principle, or the tolerance for x
    # f'(x) = (f(x+h)-f(x))/h

    #Returns: the first order differential of (cos(x)/(1-x))
    #OUTPUT = (cos(x+epsilon)/(1-(x+epsilon)) - cos(x)/(1-x))/epsilon

    #Time complexity:
    #O(20)+O(20)+O(20)+O(20)+6*O(1) = O(1)
    #Therefore time complexity = O(1)

    return (cosine(x+epsilon,20)*inverse(x+epsilon,20)-cosine(x,20)*inverse(x,20))/epsilon


#-------------------------------------------------------------------------------------------------------------#