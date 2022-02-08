### COL Assignment 1 ###
#----------------------#

from copy import deepcopy

#Part 1:

def emptyset():
    #Gives the empty set = {} representation as a list

    #Returns: [] == empty set

    return []       #O(1) time complexity
#returns [] when run


def isEmpty(S):
    #Checks whether the set is empty or not

    #Input Parameters:
    #S: list -- The representation of set S as a list containing no duplicates

    #Returns: bool -- True if the set is empty and False otherwise

    return S==emptyset()        #O(1) time complexity
#returns False when S=[1,2]


def member(S,e):
    #Checks whether e is present in the set S or not

    #Input Parameters:
    #S: list -- The representation of set S as a list containing no duplicates
    #e: same type as other elements of S -- The element to be searched for in the list

    #Returns: bool -- True if e is in S and False otherwise
    
    #Loop Invariant:
    #The index of the i element (==ind) indicates the position till where e is not present in the
    #loop. So e is not present in (0,ind-1). 
    #If it is present at ind, the function returns true and thus it wasn't in (0, ind-1).
    #If it is not present, then ind==len(S) and thus, loop invarirant is still maintained
    #as e is not in (0,len(S)-1)

    for i in S:     #Terminates as S has a finite number of elements
        if i==e:        #O(1) time to check
            return True

    #Time Complexity:
    #In the worst case, the loop runs a total of len(S) times, if e is not present n S
    #or if it is present at the last position. Therefore, the time complexity would be
    #len(S)*O(1) = O(len(S)) time complexity.

    return False
#returns True when S=[4,5,3,8,10,2] and e=2


def singleton(x):
    #Give the representation of a singleton set containg the element x

    #Input Parameters:
    #x: any type -- the singleton element in the set

    #Returns: list -- Containing single element to represent set {x}
    #OUTPUT: [x]

    return [x]      #O(1) time complexity
#returns [1] when x=1


def isSubset(P,Q):
    #Checks whether the first set is the subset of the second set or not

    #Input Parameters:
    #P: list -- The representation of set P as a list containing no duplicates
    #Q: list -- The representation of set Q as a list containing no duplicates

    #Returns: bool -- True if P is the subset of Q and False otherwise

    #Loop Invariant:
    #Till index of i element (==ind), all elements of P are present in Q.
    #If element at ind is also present in Q, then ind increases by one and the loop 
    #goes to next iteration. If it is not present, the loop stops. Therefore, loop 
    #invariant is still maintained. So after all iterations, ind==len(P) and thus all
    #elements of P are in Q and P is a subset of Q.

    for i in P:     #Terminates as there are finite number of elements in P

        if not member(Q,i):     #O(len(Q)) time to check
            return False
    
    #Time Complexity:
    #In the worst case, it runs for a total of len(P) times, if every element of P
    #is present in Q. Therefore, the time complexity is:
    #len(P)*O(len(Q)) = O(len(P)*len(Q))

    return True
#returns False when P=[1,2,0,9] and Q=[10,80,97]


def setEqual(P,Q):
    #Checks whether the sets are equal or not

    #Input Parameters:
    #P: list -- The representation of set P as a list containing no duplicates
    #Q: list -- The representation of set Q as a list containing no duplicates

    #Returns: bool -- True if P and Q are representation of same set and False otherwise

    return isSubset(P,Q) and len(P)==len(Q)     #O(len(P)*len(Q))+O(1) = O(len(P)*len(Q)) time complexity
#returns True when P=[1,8,9,0] and Q=[9,0,8,1]


def union(P,Q):
    #Gives the union of the two sets

    #Input Parameters:
    #P: list -- The representation of set P as a list containing no duplicates
    #Q: list -- The representation of set Q as a list containing no duplicates

    #Returns: list -- the representation of the set P ⋃ Q containing no duplicates

    #Representation Invariant: The lists coontain no duplicate.
    
    #Initialisation:
    T=P[:]          #O(len(P)) time to copy

    #Loop Invariant:
    #Till the i element index (==ind), T = P U Q[0:ind-1]
    #At the iteration, if ind is not in T, it is added to T, and not added if it is 
    #already present. Therefore, invariant maintains after each iteration and thus,
    #after all iterataions, T = P U Q.

    for i in Q:     #Terminates as len(Q) is finite

        if not member(P,i):     #O(len(P)) time to check
            T.append(i)         #O(1) time to append
    
    #T already contains the list P without any duplicates. Now, in the loop, only
    #the elements which aren't in P are added to T, that too as Q doen't have any
    #duplicates, thus T has no duplicates and representative invariant is maintained.

    #Time Complexity:
    #For each iteration of the loop, it takes O(len(P))+O(1)=O(len(P)) time. The loop 
    #runs for a total of len(Q) times. Therefore the total time complexity is:
    #len(Q)*O(len(P)) + O(len(P)) = O(len(P)*len(Q))

    return T
#returns [1, 2, 3, 8, 0] when P=[1,2,3] and Q=[8,2,3,0]


def intersection(P,Q):
    #Gives the intersection of the two sets

    #Input Parameters:
    #P: list -- The representation of set P as a list containing no duplicates
    #Q: list -- The representation of set Q as a list containing no duplicates

    #Returns: list -- the representation of the set P ⋂ Q containing no duplicates

    #Representation Invariant: The lists coontain no duplicate.

    #Initialisation:
    T=emptyset()    #O(1) time to initialise

    #Loop Invariant:
    #Till the i element index (==ind), T = P ⋂ Q[0:ind-1]
    #After the iteration, the element at ind index is added id it is in both P and Q
    #Otherwise it is not added. Therefore, loop invariant is maintained and thus
    #after all iterations, T = P ⋂ Q.

    for i in P:             #Terminates as the number of elements in P are finite
        if member(Q,i):     #O(len(Q)) time to check
            T.append(i)     #O(1) time

    #T was initially empty. In the loop, only the elements which are present in both
    #P and Q are added to T exactly once, and as P and Q have no repeated elements, thus
    #T doesn't have any duplicates. Therefore, the representation invariant is true.

    #Time Complexity:
    #For each iteration of the loop, it takes O(len(Q))+O(1)=O(len(Q)) time. The loop 
    #runs for a total of len(P) times. Therefore the total time complexity is:
    #len(P)*O(len(Q)) + O(len(1)) = O(len(P)*len(Q))

    return T
#returns [2,3] when P=[1,2,3] and Q=[8,2,3,0]


def cartesian(P,Q):
    #Gives the cartesian product of the two sets

    #Input Parameters:
    #P: list -- The representation of set P as a list containing no duplicates
    #Q: list -- The representation of set Q as a list containing no duplicates

    #Returns: list -- the representation of the set P x Q containing no duplicates

    #Representation Invariant: The lists coontain no duplicate.

    #Initialisation:
    T=emptyset()    #O(1) time to initialise

    #Loop Invariant 1:
    #Till the i element index (==ind1), T contains P[0:ind1-1] x Q.
    #After the iteration, All the elements P[ind] x Q are added to T. Therefore, after
    #all the iterations, ind1==len(P) and thus:
    #T = P[0:len(P)-1] x Q = P x Q.

    for i in P:                 #Terminates as len(P) is a constant

        #Loop Invariant 2:
        #Till the j element index (==ind2), T contains P[0:ind1-1] x Q[0:ind2-1].
        #After the iteration, the element (P[ind1], Q[ind2] ) is added to T. Therefore, after
        #all the iterations, ind2 == len(Q) and thus:
        #T = P[0:ind1-1] x Q[0:len(Q)-1] = P[0:ind1-1] x Q.
        
        for j in Q:             #Terminates as len(Q) is a constant
            T.append((i,j))     #O(1) time to append

    #T contains the elements (i,j) where i belongs to P and j belongs to Q.
    #As every element is appended to T only once, and moreover all i and j are 
    #different, thus T obeys the representative invariant.

    #Time Complexity:
    #The initial loop runs for a total of len(Q) times. The outer loop runs for
    #a total of len(P) times. Therefore the total time complexity is:
    #len(P)*len(Q)*O(1) = O(len(P)*len(Q))

    return T
#returns 
#[(1, 8), (1, 2), (1, 3), (1, 0), (2, 8), (2, 2), (2, 3), (2, 0), (3, 8), (3, 2), (3, 3), (3, 0)]
#when P=[1,2,3] and Q=[8,2,3,0]


def power(P):
    #Gives the power set of the input set

    #Input Parameters:
    #P: list -- The representation of set P as a list containing no duplicates

    #Returns: list -- the representation of the set power(P) containing no duplicates

    #Representation Invariant: The lists coontain no duplicate.

    #Initialisation:
    T=[[]]          #O(1) time to initialise

    #Loop Invariant 1:
    #Till index of element (==ind), T = Power set (P[0:ind-1]).
    #After each iteration, the power set T is extended to include the next element,
    #P[ind]. Therefore, after each iteration, invariant is still maintained and thus
    #after all the iterations, ind == len(P) and T == Power set of P[0:len(P)-1]
    #Therefore, T = Power Set of P

    for element in P:   #Terminates as len(P) is finite   
        A=deepcopy(T)       #O(total elements in T) time to copy

        #In this loop, the subsets containing P[ind] are created and appended to T.
        for j in A:             #Terminates as len(A) is finite
            j.append(element)   #O(1) time to append
            T.append(j)         #O(1) time to append

    #As every element appears exactly once in P, and moreover at each iteration, 
    #In T, the elements appended are unique as they are all different, so T doen't 
    #contain any duplicates. Therefore, Representative Invaraiant is true.

    #Time Complexity:
    #For each iteration of the inner loop, it takes a total of O(1)+O(1)=O(1) time.
    #Therefore, the inner loop takes len(A)*O(1) = O(len(A)) = O(len(T)) time.
    #For each iteration of the outer loop, it takes O(total elements in T)+O(len(T)) time.
    #So time complexity is O(total elements in T). 
    #Total number of sets in a set are 2^n. Counting all the elements in those set, we see
    #that each element is present in a total of 2^(n-1) subsets. Therefore:
    #Total number of elements = n*2^(n-1).
    #So, time comlexity = O(n*2^(n-1)) = O(n*2^n).

    return T
#returns [[], [3], [9], [3, 9], [0], [3, 0], [9, 0], [3, 9, 0]] when P=[3,9,0]


#-------------------------------------------------------------------------------------------------------#

#Part 2

def emptyset_2():
    #Gives the empty set {} representation as a list

    #Returns: [] = empty set

    return []       #O(1) time complexity
#returns [] always


def isEmpty_2(S):
    #Checks whether the set is empty or not

    #Input Parameters:
    #S: list -- The representation of set S as an ordered list containing no duplicates

    #Returns: bool -- True if the set is empty and False otherwise

    return S==emptyset_2()        #O(1) time complexity
#returns True when S=[]


def binary_search(S,e,first,last):
    #Checks whether the set is empty or not and returns its index

    #Input Parameters:
    #S: list -- The representation of set S as an ordered list containing no duplicates
    #e: same type as other elements of S -- The element to be searched for in the list
    #first: integer -- the minimum index where the element could be found
    #last: integer -- the maximum index where the element could be found

    #Returns: Tuple -- First element being a boolean value - True if e is in S and False 
    #                  otherwise and second element representing the index

    #Initialisation:
    found = False   #Initialisation takes O(1) time 

    #Loop Invariant:
    #Range of finding the e reduces to half after each iteration.
    #As mid lies exactly between first and last, so the range reduces to half each time.
    #After all iterations, if element is not found, the difference last-first == 0.

    while first<=last and not found:
        #Terminates as after each iteration, the difference last-first reduces to half and
        #eventually reaches 0, or either the element is found.

        mid = (first+last)//2   #bisect the interval    #O(1) Time for assigning value
        
        if S[mid]==e:           #O(1) time to check
            return True,mid
        
        elif S[mid]<e:          #O(1) time to check
            first=mid+1         #O(1) time to update
        
        else:                   #O(1) time to check
            last=mid-1          #O(1) time to update

    #Time Complexity:
    #At every situation, the value of last-first reduces to half untill they become equal, 
    #after which the loop ends. Therefore the time complexity is
    #O(log(last - first)), where last and first were the input values.

    return False,first
#returns (True,2) when S=[1,2,3], e=3, first=0, last=2


def member_2(S,e):
    #Checks whether e is present in the set S or not

    #Input Parameters:
    #S: list -- The representation of set S as an ordered list containing no duplicates
    #e: same type as other elements of S -- The element to be searched for in the list

    #Returns: bool -- True if e is in S and False otherwise

    #Initialisation
    first=0             #O(1) time
    last=len(S)-1       #O(1) time

    #Time Complexity:
    #O(log(last-first)) = O(log(len(S)))

    return binary_search(S,e,first,last)[0]
#returns True when S=[1,2,3] and e=3


def singleton_2(x):
    #Give the representation of a singleton set containg the element x = {x}

    #Input Parameters:
    #x: any type -- the singleton element in the set

    #Returns: list -- Containing single element to represent set
    #OUTPUT: [x]

    return [x]      #O(1) time complexity
#returns [2] when x=2


def isSubset_2(P,Q):
    #Checks whether the first set is the subset of the second set or not

    #Input Parameters:
    #P: list -- The representation of set P as an ordered list containing no duplicates
    #Q: list -- The representation of set Q as an ordered list containing no duplicates

    #Returns: bool -- True if P is the subset of Q and False otherwise

    #Initialisation:
    first=0         #O(1) time
    last=len(Q)-1   #O(1) time

    #Loop Invariant:
    #Till the i element index (==ind), the elements of P[0:ind-1] are all 
    #present in Q. That is P[0,ind-1] is subset of Q.
    #After the next iteration, if ind is not present, the loop stops and the invariant is
    #maintained. If the loop continues, then ind+=1 and still the invariant maintains.
    #Therefore after all itereations ind==len(P) and thus,
    #P[0:len(P)-1] is subset of Q ==> P is subset of Q.

    for i in P:     #Terminates as len(P) is finite

        A=binary_search(Q,i,first,last)     #O(log(last-first)) time

        if not A[0]:                        #O(1) time to check
            return False

        else:
            first=A[1]+1                    #O(1) time to check

    #Time Complexity:
    #For each iteration, the time complexity is O(log(last-first)). Therefore worst time 
    #complexity is when all the elements of P are present in Q. So time complexity is:
    #len(P)*O(log(last-first)) = O(log(len(Q))*len(P))

    return True
#returns True when P=[4,5,6] and Q=[1,4,5,6,7]


def setEqual_2(P,Q):
    #Checks whether the sets are equal or not

    #Input Parameters:
    #P: list -- The representation of set P as an ordered list containing no duplicates
    #Q: list -- The representation of set Q as an ordered list containing no duplicates

    #Returns: bool -- True if P==Q and False otherwise

    return P==Q     #O(min(len(P),len(Q))) time to check
#returns False when P=[3,4,5] and Q=[5,6,7]


def union_2(P,Q):
    #Gives the union of the two sets

    #Input Parameters:
    #P: list -- The representation of set P as an ordered list containing no duplicates
    #Q: list -- The representation of set Q as an ordered list containing no duplicates

    #Returns: list -- the representation of the set P ⋃ Q as an ordered list containing no duplicates

    #Representation Invariant: The lists coontain no duplicate and are ordered.

    #Initialisation:        #O(1) time complexity
    T=[]
    i=0
    j=0
    
    #Loop Invariant:
    #T will contain i+j-n elements in sorted order, n=number of equal elements obtained till now.
    #After each iteration, the samller of the element, either P[i] or Q[j] will be added
    #to the list T. But it will still be greater than the last element already present in T.
    #Then, i+j would be updated by 1, if P[i] and Q[j] were different, or by 2 if thery were same.
    #n would be updated by 1 if they were same. In each case, the invariant maintains.

    while i!=len(P) and j!=len(Q):     #Terminates as atleast i or j will become equal to length

        if P[i]<Q[j]:       #O(1) time to check
            T.append(P[i])  #O(1) time
            i+=1            #O(1) time

        elif P[i]>Q[j]:     #O(1) time to check
            T.append(Q[j])  #O(1) time
            j+=1            #O(1) time

        else:
            T.append(P[i])  #O(1) time
            i+=1            #O(1) time
            j+=1            #O(1) time
    #Overall time for loop = O(min(len(P),len(Q))), the number of times the iteration happens.

    if j==len(Q):           #O(1) time
        T.extend(P[i:])     #O(len(P)-i)

    else:
        T.extend(Q[j:])     #O(len(Q)-j)

    #In the loop, the element added is the least element from P and Q in each iteration. Therefore
    #the next element is always greater than the previous. Moreover as P and Q have all unique
    #elements, therefore T is also sorted and contain no duplicates.
    #Therefore the representative invariant is observed.

    #Time Complexity:
    #Adding the times of loop and the if else statement, we obtain the time complexity as:
    #O(max(len(P),len(Q))) as we are iterating both the arrays exactly one time.

    return T
#returns [1, 4, 5, 6, 7, 8] when P=[4,7,8] and Q=[1,4,5,6,7]


def intersection_2(P,Q):
    #Gives the intersection of the two sets

    #Input Parameters:
    #P: list -- The representation of set P as an ordered list containing no duplicates
    #Q: list -- The representation of set Q as an ordered list containing no duplicates

    #Returns: list -- the representation of the set P ⋂ Q as an ordered list containing no duplicates

    #Representation Invariant: The lists coontain no duplicate and are ordered.

    #Initialisation:        #O(1) time
    T=[]
    first=0
    last=len(Q)-1
    
    #Loop Invariant:
    #Till the index of i elemnet(==ind), the intersecting elements are apended in T,
    #i.e. T contains P[0:ind-1] ⋂ Q.
    #After the iteration, the element is added if it is present in both P and Q, otherwise
    #it is not added. Therefore, after the iteration, the loop invariant still remains.
    #So, after all the iterations, ind==len(P), and thus:
    #T = P[0:len(P)-1] ⋂ Q  = P ⋂ Q

    for i in P:         #Terminates as len(P) is finite
        if binary_search(Q,i,first,last)[0]:    #O(log(last-first)) time
            T.append(i)                         #O(1) time
    
    #T was initially empty. In the loop, only the elements which are present in both
    #P and Q are added to T exactly once and the least element is added first, and
    #the next elements are always greater. As P and Q have no repeated elements, thus
    #T doesn't have any duplicates. Therefore, the representation invariant is true. 

    #Time Complexity:
    #For each iteration of the loop, it takes O(log(last-first)) time. The loop 
    #runs for a total of len(P) times. Therefore the total time complexity is:
    #len(P)*O(log(last-first)) = O(len(P)*log(len(Q)))
    
    return T
#returns [4,7] when P=[4,7,8] and Q=[1,4,5,6,7]


def cartesian_2(P,Q):
    #Gives the cartesian product of the two sets

    #Input Parameters:
    #P: list -- The representation of set P as an ordered list containing no duplicates
    #Q: list -- The representation of set Q as an ordered list containing no duplicates

    #Returns: list -- the representation of the set P x Q as an ordered list containing no duplicates

    #Representation Invariant: The lists coontain no duplicate and are ordered.

    #Initialisation:
    T=emptyset_2()    #O(1) time to initialise

    #Loop Invariant 1:
    #Till the i element index (==ind1), T contains P[0:ind1-1] x Q.
    #After the iteration, All the elements P[ind] x Q are added to T. Therefore, after
    #all the iterations, ind1==len(P) and thus:
    #T = P[0:len(P)-1] x Q = P x Q.

    for i in P:             #Terminates as len(P) is a constant
        
        #Loop Invariant 2:
        #Till the j element index (==ind2), T contains P[0:ind1-1] x Q[0:ind2-1].
        #After the iteration, the element (P[ind1], Q[ind2] ) is added to T. Therefore, after
        #all the iterations, ind2 == len(Q) and thus:
        #T = P[0:ind1-1] x Q[0:len(Q)-1] = P[0:ind1-1] x Q.
        
        for j in Q:         #Terminates as len(Q) is a constant
            T.append((i,j))     #O(1) time to append

    #T contains the elements (i,j) where i belongs to P and j belongs to Q.
    #As every element is appended to T only once, and moreover all i and j are 
    #different, with the least value of i added first, and P and Q also being 
    #sorted thus T obeys the representative invariant.

    #Time Complexity:
    #The initial loop runs for a total of len(Q) times. The outer loop runs for
    #a total of len(P) times. Therefore the total time complexity is:
    #len(P)*len(Q)*O(1) = O(len(P)*len(Q))
    #This time complexity is the best possible, as any alg would have to append atleast
    #len(P)*len(Q) elements to the list for the ans.

    return T
#returns
#[(1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)]
#when P=[1,2,3] and Q=[2,3]


def power_2(P):
    #Gives the power set of the input set

    #Input Parameters:
    #P: list -- The representation of set P as an ordered list containing no duplicates

    #Returns: list -- the representation of the set power(P) as an ordered list containing no duplicates

    #Representation Invariant: The lists coontain no duplicate and are ordered.

    #Inititalisation:
    T=[[]]      #O(1) time to initialise

    if len(P)!=0:               #O(1) time to check
        
        A=power_2(P[1:])        #T(n-1) time
        first=P[0]              #O(1) time
        B=deepcopy(A[1:])       #O(number of elements in A)=O((n-1)*2^(n-1))

        for i in A:
            i.insert(0,first)   #O(len(i)) time for each iteration
        #Total time for loop = O(number of elements in A)
        #Time = O((n-1)*2^(n-1))
        
        T.extend(A)             #O(len(A)) time
        T.extend(B)             #O(len(B)) time = O(len(A))

    #As every element appears exactly once in P, and moreover at each iteration, 
    #in T, the elements appended are unique as they are all different, so T doesn't 
    #contain any duplicates. As the base case of T is sorted, and when new elements 
    #are inserted to T, they are too sorted, therefore T is also sorted. So, the
    #representative invariant is observed.

    #Time Complexity:
    #T(n) = T(n-1) + O((n-1)*2^(n-1))
    #Solving the relation, we get T(n) = O((n-2)*2^n)
    #Therefore, the time complexity = O(n*2^n)
    #As similarly stated in power() function, this time complexity is the best possible, 
    #if we disregard the constant factors.

    return T
#returns [[], [4], [4, 5], [4, 5, 6], [4, 6], [5], [5, 6], [6]] when P=[4,5,6]
