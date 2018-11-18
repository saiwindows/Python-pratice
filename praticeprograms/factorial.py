#algorithm
#tep1: take input from the user
#step2: multiply the input with previous number to input
#step3:print the factorail of the input


factnum=int(input("enter a factorial numberfact"))
factorail=1
if factnum < 0:
    print(factnum,"no factorail for this number")
elif factnum==0:
    print(factnum," is 1")
else:
    for i in range(1,factnum+1):
        factorail=factorail*i
        print("the factorail of ",factnum ,"is",factorail )
