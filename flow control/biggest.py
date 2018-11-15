#write a python program to find the biggest number from given 3 numbers

num1=int(input("enter a first number:\t"))
num2=int(input("enter a second number:\t"))
num3=int(input("enter a third number:\t"))
if num1>num2 and num1>num3:
    print("first number is the biggest",num1)
elif num2>num1 and num2>num3:
    print("second number is the biggest",num2)
else:
    print("third number is the biggest",num3)
