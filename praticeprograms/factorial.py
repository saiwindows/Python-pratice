#algorithm
#tep1: take input from the user
#step2: multiply the input with previous number to input
#step3:print the factorial of the input


factnum=int(input("enter a factorial numberfact"))
factorial=1
if factnum < 0:
    print(factnum,"no factorial for this number")
elif factnum==0:
    print(factnum," is 1")
else:
    for i in range(1,factnum+1):# factnum is used for increments i value same as given in input
        factorial=factorial*i  # to multipy
        print("the factorial of ",factnum ,"is",factorial )
