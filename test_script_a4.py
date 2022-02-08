import importlib, sys, traceback, re
from glob import glob
fileNameRegex = re.compile('[0-9]{4}[a-zA-Z]{2}[0-9]{5}_assignment_4\.py')

files = glob("*_assignment_4.py")

if len(files)==0:
    print('Enter the file in correct format. Expected = <entryNumber>_assignment_3.py')
    sys.exit(1)

file = files[0]

m = fileNameRegex.match(file)

if m == None:
    print(f'Enter the file in correct format. Found = {file}. Expected = <entryNumber>_assignment_3.py')
    sys.exit(1)

print("Found file: ",file)
file = file[:-3]


col100_module = importlib.import_module(file)
import math

# Test cases ---- [Input, Expected Output, User Output] 

def check_set(s,l):
    b = []
    for i in l:
        if i in b:
            return False
        b.append(i)
    return (set(b) == s)

def check_set_power(l1,l2):
    b = []
    for i in l1:
        b.append(set(i))
    for i in l2:
        found = False
        for j in range(0,len(b)):
            if(check_set(b[j],i)):
                found = True
                del b[j]
                break
        if not found:
            return False
    return (len(b) == 0)

def helper(fn):
    s = '-' * 30
    print (f'\n{s} Testing for {fn} {s}')

def test_emptyset():
    helper("emptyset")
    user_output = col100_module.emptyset()
    print(f'Function: emptyset, Verdict: {len(user_output) == 0}')

def test_isEmpty():
    helper("isEmpty")
    xl = [[], [1,2,4]]
    expected_output = [True, False]
    user_output = [col100_module.isEmpty(x) for x in xl]
    for i in range(0,len(xl)):
        print(f'Function: isEmpty, Input: {xl[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_member():
    helper("member")
    x1l = [[],[(4,"mtl"),(4,"col"),(2,"cmp")]]
    x2l = [2,(4,"col")]
    expected_output = [False, True]
    user_output = [col100_module.member(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: member, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_singleton():
    helper("singleton")
    xl = [0.0,"Alan Turing"]
    expected_output = [[0.0],["Alan Turing"]]
    user_output = [col100_module.singleton(x) for x in xl]
    for i in range(0,len(xl)):
        print(f'Function: singleton, Input: ({xl[i]})\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_isSubset():
    helper("isSubset")
    x2l = [["Yudhishthir", "Bhim", "Arjun", "Nakul", "Sahadev"],[(0,"Aryabhatta "), (1729,"Ramanujan")]]
    x1l = [["Arjun","Karn"],[(0,"Aryabhatta ")]]
    expected_output = [False, True]
    user_output = [col100_module.isSubset(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: isSubset, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_setEqual():
    helper("setEqual")
    x1l = [["virat","dhoni","sachin","rohit"], [1.0,-1.0],[]]
    x2l = [["scahin","dhoni","virat","rohit"],[-1.0,1.0],["its empty"]]
    expected_output = [True, True, False]
    user_output = [col100_module.setEqual(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: setEqual, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_union():
    helper("union")
    x1l = [["virat","sachin"], [1.0,-1.0,2.0,3.0]]
    x2l = [["dhoni","bumrah"],[-1.0,1.0]]
    expected_output = [["virat","dhoni","sachin","bumrah"], [1.0,-1.0,2.0,3.0]]
    user_output = [col100_module.union(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: union, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {check_set(set(expected_output[i]),user_output[i])}')

def test_intersection():
    helper("intersection")
    x1l = [["delhi","mumbai","banglore"], [1.0,-1.0,2.0,3.0]]
    x2l = [["delhi","kolkata"],[-1.0,1.0]]
    expected_output = [["delhi"], [1.0,-1.0]]
    user_output = [col100_module.intersection(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: intersection, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {check_set(set(expected_output[i]),user_output[i])}')

def test_cartesian():
    helper("cartesian")
    x1l = [[1,2,3], [2,1]]
    x2l = [[1],["a","b"]]
    expected_output = [[(1,1),(2,1),(3,1)], [(2,"a"),(1,"a"),(1,"b"),(2,"b")], []]
    user_output = [col100_module.cartesian(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: cartesian, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {check_set(set(expected_output[i]),user_output[i])}')


def test_power():
    helper("power")
    x1l = [[1,2,3], [2,1]]
    expected_output = [[[],[1],[2],[3],[1,2],[1,3],[3,2],[1,2,3]],[[],[2],[1],[1,2]]]
    user_output = [col100_module.power(x1l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: power, Input: {x1l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {check_set_power(expected_output[i],user_output[i])}')

def test_emptyset_2():
    helper("emptyset_2")
    user_output = col100_module.emptyset_2()
    print(f'Function: emptyset_2, Verdict: {len(user_output) == 0}')

def test_isEmpty_2():
    helper("isEmpty_2")
    xl = [[], [1,2,4]]
    expected_output = [True, False]
    user_output = [col100_module.isEmpty_2(x) for x in xl]
    for i in range(0,len(xl)):
        print(f'Function: isEmpty_2, Input: {xl[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_member_2():
    helper("member_2")
    x1l = [[],[(2,"cmp"),(4,"col"),(4,"mtl")]]
    x2l = [2,(4,"col")]
    expected_output = [False, True]
    user_output = [col100_module.member_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: member_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_singleton_2():
    helper("singleton_2")
    xl = [0.0,(2,"cmp")]
    expected_output = [[0.0],[(2,"cmp")]]
    user_output = [col100_module.singleton_2(x) for x in xl]
    for i in range(0,len(xl)):
        print(f'Function: singleton_2, Input: ({xl[i]})\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_isSubset_2():
    helper("isSubset_2")
    x2l = [["Arjun","Bhim" ,"Nakul","Sahadev","Yudhishthir"],[(0,"Aryabhatta "), (1729,"Ramanujan")]]
    x1l = [["Arjun","Karn"],[(0,"Aryabhatta "),(1729,"Ramanujan")]]
    expected_output = [False, True]
    user_output = [col100_module.isSubset(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: isSubset_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_setEqual_2():
    helper("setEqual_2")
    x1l = [["dhoni","rohit","sachin","virat"], [-1.0,1.0]]
    x2l = [["dhoni","rohit","sachin"],[-1.0,1.0]]
    expected_output = [False, True]
    user_output = [col100_module.setEqual_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: setEqual_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_union_2():
    helper("union_2")
    x1l = [["sachin","virat"], [-1.0,1.0,2.0,3.0]]
    x2l = [["bumrah","dhoni"],[-1.0,1.0]]
    expected_output = [["bumrah","dhoni","sachin","virat"], [-1.0,1.0,2.0,3.0]]
    user_output = [col100_module.union_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: union_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_intersection_2():
    helper("intersection_2")
    x1l = [["banglore","delhi","mumbai"], [-1.0,1.0,2.0,3.0]]
    x2l = [["delhi","kolkata"],[-1.0,1.0]]
    expected_output = [["delhi"], [-1.0,1.0]]
    user_output = [col100_module.intersection_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: intersection_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

def test_cartesian_2():
    helper("cartesian_2")
    x1l = [[1,2,3], [1,2]]
    x2l = [[1],["a","b"]]
    expected_output = [[(1,1),(2,1),(3,1)], [(1,"a"),(1,"b"),(2,"a"),(2,"b")]]
    user_output = [col100_module.cartesian_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: cartesian_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')


def test_power_2():
    helper("power_2")
    x1l = [[1,2,3], [1,2]]
    expected_output = [[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]],[[],[1],[1,2],[2]]]
    user_output = [col100_module.power_2(x1l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        print(f'Function: power_2, Input: {x1l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output[i]}, Verdict: {expected_output[i] == user_output[i]}')

##############################################################################################################################################################
#DO NOT TOUCH ANY CODE LINE ABOVE THIS

# uncomment the below to test for problem 1 to 6

helper("Part 1")
try:
    test_emptyset() 			
except Exception as e:
    print(traceback.format_exc())    

try:
    test_isEmpty()
except Exception as e:
    print(traceback.format_exc())  

try:
    test_member()
except Exception as e:
    print(traceback.format_exc())  

try:
    test_singleton()
except Exception as e:
    print(traceback.format_exc())

try:
    test_isSubset()
except Exception as e:
    print(traceback.format_exc())


try:
    test_union()
except Exception as e:
    print(traceback.format_exc())

try:
    test_intersection()
except Exception as e:
    print(traceback.format_exc())

try:
    test_cartesian()
except Exception as e:
    print(traceback.format_exc())

try:
    test_power()
except Exception as e:
    print(traceback.format_exc())

helper("Part 2") 

try:
    test_emptyset_2()             
except Exception as e:
    print(traceback.format_exc())    

try:
    test_isEmpty_2()
except Exception as e:
    print(traceback.format_exc())  

try:
    test_member_2()
except Exception as e:
    print(traceback.format_exc())  

try:
    test_singleton_2()
except Exception as e:
    print(traceback.format_exc())

try:
    test_isSubset_2()
except Exception as e:
    print(traceback.format_exc())

try:
    test_union_2()
except Exception as e:
    print(traceback.format_exc())

try:
    test_intersection_2()
except Exception as e:
    print(traceback.format_exc())

try:
    test_cartesian_2()
except Exception as e:
    print(traceback.format_exc())

try:
    test_power_2()
except Exception as e:
    print(traceback.format_exc())