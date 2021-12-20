#Checker
#Loops over all the various possible inputs and checks whether the output is correct or not.

def integer(t,n):
    #Converts the tuple output to integer
    ans =0
    for i in range(n):
        ans+=(t[i]*pow(2,i))
    return ans

l=[False,True]    #List for looping

marks = 0

#1) Full adder
print("Checking Funtion: full adder") 
error=0
for a in l:
    for b in l:
        for c in l:
            k=add(a,b,c)
            if a+b+c!=integer(k,2):
                error+=1
                print("Error when:")
                print(a,'+',b,'+',c,'=',k)
if error==0:
    marks+=1
print("Function 1 -- full adder checked")
print(error,"Errors found.\n")

#2) add4
print("Checking Funtion: add4") 
error=0
for a3 in l:
    for a2 in l:
        for a1 in l:
            for a0 in l:
                for b3 in l:
                    for b2 in l:
                        for b1 in l:
                            for b0 in l:
                                for c in l:
                                    k=add4(a0,a1,a2,a3, b0,b1,b2,b3, c)
                                    a=integer((a0,a1,a2,a3),4)
                                    b=integer((b0,b1,b2,b3),4)
                                    if a+b+c!=integer(k,5):
                                        error+=1
                                        print("Error when:")
                                        print(a,'+',b,'+',c,'=',k)
if error==0:
    marks+=1
print("Function 2 -- add4 checked")
print(error,"Errors found.\n")

#3) cmp
print("Checking Funtion: cmp") 
enum = int(input("Enter the last 2 digits of entry number: "))
enum=enum%4
error =0
for a3 in l:
    for a2 in l:
        for a1 in l:
            for a0 in l:
                for b3 in l:
                    for b2 in l:
                        for b1 in l:
                            for b0 in l:
                                k=cmp(a0,a1,a2,a3, b0,b1,b2,b3)
                                a=integer((a0,a1,a2,a3),4)
                                b=integer((b0,b1,b2,b3),4)
                                if enum==0:
                                    if (a<b)!=k:
                                        error+=1
                                        print("Error when:")
                                        print(a,'<',b,'=',k)
                                elif enum==1:
                                    if (a<=b)!=k:
                                        error+=1
                                        print("Error when:")
                                        print(a,'<=',b,'=',k)
                                elif enum==2:
                                    if (a>b)!=k:
                                        error+=1
                                        print("Error when:")
                                        print(a,'>',b,'=',k)
                                else:
                                    if (a>=b)!=k:
                                        error+=1
                                        print("Error when:")
                                        print(a,'>=',b,'=',k)
if error==0:
    marks+=1
print("Function 3 -- comparator checked")
print(error,"Errors found.\n")

#4) sub4
print("Checking Funtion: sub4") 
error=0
for a3 in l:
    for a2 in l:
        for a1 in l:
            for a0 in l:
                for b3 in l:
                    for b2 in l:
                        for b1 in l:
                            for b0 in l:
                                k=sub4(a0,a1,a2,a3, b0,b1,b2,b3)
                                a=integer((a0,a1,a2,a3),4)
                                b=integer((b0,b1,b2,b3),4)
                                if a-b!=pow(-1,k[4])*integer(k,4):
                                    error+=1
                                    print("Error when:")
                                    print(a,'-',b,'=',k)
if error==0:
    marks+=1
print("Function 4 -- subtractor checked")
print(error,"Errors found.\n")

#5) add8
print("Checking Funtion: add8") 
error=0
for a7 in l:
    for a6 in l:
        for a5 in l:
            for a4 in l:
                for a3 in l:
                    for a2 in l:
                        for a1 in l:
                            for a0 in l:
                                for b7 in l:
                                    for b6 in l:
                                        for b5 in l:
                                            for b4 in l:
                                                for b3 in l:
                                                    for b2 in l:
                                                        for b1 in l:
                                                            for b0 in l:
                                                                for c in l:
                                                                    a=(a0,a1,a2,a3,a4,a5,a6,a7)
                                                                    b=(b0,b1,b2,b3,b4,b5,b6,b7)
                                                                    (k,r)=add8(a,b,c)
                                                                    int1=integer(a,8)
                                                                    int2=integer(b,8)
                                                                    int3=integer(k,8)+pow(2,8)*r
                                                                    if int1+int2+c!=int3:
                                                                        error+=1
                                                                        print("Error when:")
                                                                        print(a,'+',b,'+',c,'=',(k,r))
if error==0:
    marks+=1
print("Function 5 -- add8 checked")
print(error,"Errors found.\n")


#6) mul4
print("Checking Funtion: mul4") 
error=0
for a3 in l:
    for a2 in l:
        for a1 in l:
            for a0 in l:
                for b3 in l:
                    for b2 in l:
                        for b1 in l:
                            for b0 in l:
                                a=(a0,a1,a2,a3)
                                b=(b0,b1,b2,b3)
                                int1=integer(a,4)
                                int2=integer(b,4)
                                k=mul4(a,b)
                                int3=integer(k,8)
                                if int1*int2!=int3:
                                    error+=1
                                    print("Error when:")
                                    print(a,'*',b,'=',k)
if error==0:
    marks+=1
print("Function 6 -- mul4 checked")
print(error,"Errors found.\n")

print("Test Completed. Thanks for using this code.")
print("Marks obtained =", marks,"/ 6")
print("Now go and study for MTL.")
