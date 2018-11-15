for i in range (4):
    print("i")
    # output is i,i,i,i

for i in range(4,8):
    print("i")

    # output is i,i,i,i
    # because range function will execute i's from 4 to 8

    for i in range(4,8,2):
        print("i")

    # here range function will exeute 3 i's because 2 defines the range from 4 to 8
