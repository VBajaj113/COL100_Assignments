import importlib, sys, traceback, re
from glob import glob
fileNameRegex = re.compile('[0-9]{4}[a-zA-Z]{2}[0-9]{5}_assignment_3\.py')

files = glob("*_assignment_3.py")

if len(files)==0:
    print('Enter the file in correct format. Expected = <entryNumber>_assignment_3.py')
    sys.exit(1)

file = files[0]

m = fileNameRegex.match(file)

if m == None:
    print(f'Enter the file in correct format. Found = {file}. Expected = <entryNumber>_assignment_3.py')
    sys.exit(1)

file = file[:-3]
entry_number = file.split('_', 1)[0]

rem = int(entry_number[7:]) % 4


col100_module = importlib.import_module(file)
import math

# Test cases ---- [Input, Expected Output, User Output] 

def isSame(a, b):
    s = '-' * 90
    diff = abs(a-b) 
    if (diff <= 1e-6):
        return "TEST PASSED\n" + s
    else:
        return "TEST FAILED\n" + s

def helper(n):
    s = '-' * 30
    print (f'\n{s} Testing for problem {n} {s}')

def test_q1():
    input = [(1,26), (0.5,4), (0,90), (math.pi/2,6), (0,100), (0.5,5), (0, 100), (0.8, 8), (0, 30), (1, 4) ]
    act_output = [2.718281, 1.645833, 1.000000, -4.647660083659713e-07, 1.000000,1.937500, 0.0, 0.579099, 0.0, 0.723809]
    user_output = [col100_module.expn(1,26), col100_module.expn(0.5,4), col100_module.cosine(0,90), col100_module.cosine(math.pi/2,6), col100_module.inverse(0,100), col100_module.inverse(0.5,5), col100_module.natural_log(0, 100), col100_module.natural_log(0.8, 8), col100_module.tan_inv(0,30), col100_module.tan_inv(1,4)]  
    desc = ['expn', 'expn', 'cosine', 'cosine', 'inverse', 'inverse', 'natural_log', 'natural_log', 'tan_inv', 'tan_inv']
    
    helper(1)
    for i in range(len(input)):
        print(f'Function: {desc[i]}, Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')

def q2_functions(x, func):
  if func == 0:
    return math.cos(x) + math.exp(-x)
  elif func == 1:
    return math.exp(-x) - math.sin(x)
  elif func == 2:
    return math.sin(x) + 1/(1-x)
  elif func == 3:
    return 1/(1-x) - math.cos(x)

def verify_q2(found, value, iterList, eps, func):
    if found == True and abs(q2_functions(value, func)) <= eps:
        return "TEST PASSED\n" + ('-' * 90)
    else:
        return "TEST FAILED\n" + ('-' * 90)

def test_q2():
    helper(2)
    if rem == 0:
        input = [(0, 3, 0.1), (3, 5, 1)]
        
        for i in range(len(input)):
            (found, value, iterList) = col100_module.bisect(*input[i])
            print(f'Input: {input[i]}\nUser Output: {(found, value, iterList)}, Verdict: {verify_q2(found, value, iterList, input[i][2], rem)}')
    elif rem == 1:
        input = [(2, 4, 0.1), (11, 20, 0.01)]
    
        for i in range(len(input)):
            (found, value, iterList) = col100_module.bisect(*input[i])
            print(f'Input: {input[i]}\nUser Output: {(found, value, iterList)}, Verdict: {verify_q2(found, value, iterList, input[i][2], rem)}')
    elif rem == 2:
        input = [(4.637, 7.874, 0.1), (-2.112, 0.567, 0.5)]
    
        for i in range(len(input)):
            (found, value, iterList) = col100_module.bisect(*input[i])
            print(f'Input: {input[i]}\nUser Output: {(found, value, iterList)}, Verdict: {verify_q2(found, value, iterList, input[i][2], rem)}')
    else:
        input = [(2.936, 6.247, 0.5), (7.51, 9.439, 0.005)]
    
        for i in range(len(input)):
            (found, value, iterList) = col100_module.bisect(*input[i])
            print(f'Input: {input[i]}\nUser Output: {(found, value, iterList)}, Verdict: {verify_q2(found, value, iterList, input[i][2], rem)}')


def test_q3():
    input = [0, 2, 0, 2, 0, 5, 0, 4, 8, 9]
    act_output = [1.0, 0.5, 1.000000, -0.5, 1.000000,1.00, 0.0, -0.25, 0.0, 0.1111111]
    user_output = [col100_module.expn_coeff(0), col100_module.expn_coeff(2), col100_module.cosine_coeff(0), col100_module.cosine_coeff(2), col100_module.inverse_coeff(0), col100_module.inverse_coeff(5), col100_module.natural_log_coeff(0), col100_module.natural_log_coeff(4), col100_module.tan_inv_coeff(8), col100_module.tan_inv_coeff(9)]
    desc = ['expn_coeff', 'expn_coeff', 'cosine_coeff', 'cosine_coeff', 'inverse_coeff', 'inverse_coeff', 'natural_log_coeff', 'natural_log_coeff', 'tan_inv_coeff', 'tan_inv_coeff']  
    
    helper(3)
    for i in range(len(input)):
        print(f'Function: {desc[i]}, Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')


def test_q4():     
    input = [(0,5), (1,3), (0,1), (math.pi/2,5), 0, 5, (1,0), (2,5), (0,0), (0.5,5)]
    act_output = [1.0, 2.666666, 1.000000, 0.019968, 1.000000,1.75, 0.0, 5.0666666, 0.0, 0.4645833]
    user_output = [col100_module.expn_t(0,5), col100_module.expn_t(1,3), col100_module.cosine_t(0,1), col100_module.cosine_t(math.pi/2,5), col100_module.inverse_t(1,0), col100_module.inverse_t(0.5,2), col100_module.natural_log_t(1,0), col100_module.natural_log_t(2,5), col100_module.tan_inv_t(0,0), col100_module.tan_inv_t(0.5,5)]
    desc = ['expn_t', 'expn_t', 'cosine_t', 'cosine_t', 'inverse_t', 'inverse_t', 'natural_log_t', 'natural_log_t', 'tan_inv_t', 'tan_inv_t']  
    
    helper(4)
    for i in range(len(input)):
        print(f'Function: {desc[i]}, Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')


def test_q5():
    
    if (rem == -1):
        print ("\nPlease update the value of rem in this file")
    else:
        helper(5)
    if rem == 0:
      
        input = [0,2,0,2,0,5]
        act_output = [1.0, -1.0, 0.0, -0.5, 0.0, -0.008333]
        user_output = [col100_module.add_coeff(0), col100_module.add_coeff(2), col100_module.mul_coeff(0), col100_module.mul_coeff(2), col100_module.diff_coeff(0),col100_module.diff_coeff(5)]
        desc = ['add_coeff', 'add_coeff', 'mul_coeff', 'mul_coeff', 'diff_coeff', 'diff_coeff']  
        for i in range(len(input)):
            print(f'Function: {desc[i]}, Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')

    elif rem == 1:
        
        input = [0,5,0,1,0,5]
        act_output = [2.0, 0.9916666, 1.0, 0.0, -1.0, 0.008333]
        user_output = [col100_module.add_coeff(0), col100_module.add_coeff(5), col100_module.mul_coeff(0), col100_module.mul_coeff(1), col100_module.diff_coeff(0),col100_module.diff_coeff(5)]
        desc = ['add_coeff', 'add_coeff', 'mul_coeff', 'mul_coeff', 'diff_coeff', 'diff_coeff']    
        for i in range(len(input)):
            print(f'Function: {desc[i]}, Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')

    elif rem == 2:
        
        input = [0,5,0,1,0,5]
        act_output = [2.0, 0.9916666, 1.0, 0.0, 1, 6]
        user_output = [col100_module.add_coeff(0), col100_module.add_coeff(5), col100_module.mul_coeff(0), col100_module.mul_coeff(1), col100_module.diff_coeff(0),col100_module.diff_coeff(5)]
        desc = ['add_coeff', 'add_coeff', 'mul_coeff', 'mul_coeff', 'diff_coeff', 'diff_coeff']    
        for i in range(len(input)):
            print(f'Function: {desc[i]}, Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')
    
    elif rem == 3:
        
        input = [0, 2, 0, 2, 0, 5]
        act_output = [1.0, -1.0, 0.0, -0.5, 1.0,-1]
        user_output = [col100_module.add_coeff(0), col100_module.add_coeff(2), col100_module.mul_coeff(0), col100_module.mul_coeff(2), col100_module.diff_coeff(0),col100_module.diff_coeff(5)]
        desc = ['add_coeff', 'add_coeff', 'mul_coeff', 'mul_coeff', 'diff_coeff', 'diff_coeff']    
        for i in range(len(input)):
            print(f'Function: {desc[i]}, Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')



def test_q6():
    if (rem == -1):
        print ("\nPlease update the value of rem in this file")
    else:
        helper(6)
        
    if rem == 0:
        input = [(math.pi/4,0.001),(-math.pi/4,0.000001)]
        act_output = [2.002002,1.999997]
        user_output = [col100_module.limit_diff(math.pi/4,0.001), col100_module.limit_diff(-math.pi/4,0.000001)
                    ]  
        for i in range(len(input)):
            print(f'Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')

    elif rem == 1:

        input = [(0,0.000000001),(math.pi/2,0.000000000000001) ]
        act_output = [0.999999, -0.277555]
        user_output = [col100_module.limit_diff(0,0.000000001),col100_module.limit_diff(math.pi/2,0.000000000000001)
                    ]  
        for i in range(len(input)):
            print(f'Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')

    elif rem == 2:
        
        input = [(0,0.000001), (math.pi/4,0.0001)]
        act_output = [ 1.0,11.297830]
        user_output = [ col100_module.limit_diff(0,0.000001),col100_module.limit_diff(math.pi/4,0.0001)
                    ]  
        for i in range(len(input)):
            print(f'Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')
   
    elif rem == 3:

        input = [(0,0.000001),(0,0.0001) ]
        act_output = [0.999999,0.999949]
        user_output = [col100_module.limit_diff(0,0.000001),col100_module.limit_diff(0,0.0001)
                    ]  
        for i in range(len(input)):
            print(f'Input: {input[i]}\nExpected Output: {act_output[i]} User Output: {user_output[i]}, Verdict: {isSame(act_output[i], user_output[i])}')



##############################################################################################################################################################
#DO NOT TOUCH ANY CODE LINE ABOVE THIS

# uncomment the below to test for problem 1 to 6
try:
    test_q1() 					# problem 1
except Exception as e:
    print(traceback.format_exc())    

try:
    test_q2() 					# problem 2
except Exception as e:
    print(traceback.format_exc())  

try:
    test_q3() 					# problem 3
except Exception as e:
    print(traceback.format_exc())  
try:
    test_q4() 					# problem 4
except Exception as e:
    print(traceback.format_exc())          

try:
    test_q5() 					# problem 5
except Exception as e:
    print(traceback.format_exc())  

try:
    test_q6() 					# problem 6
except Exception as e:
    print(traceback.format_exc())  
