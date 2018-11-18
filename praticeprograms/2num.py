prime=int(input("enter a number to check whether it is prime or not \n"))
if (prime > 1):
    for i in range(2,prime-1):
        if(prime%i)==0:
            print(prime,"not a prime number")
            break
    else:
         print(prime,"prime number")
else:
    print(prime,"not a prime number")