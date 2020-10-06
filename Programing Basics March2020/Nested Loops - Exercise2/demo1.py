number = int(input())
macig = True



for num in range(1111 , 9999 + 1):
    num_as_sting = str(num)
    for i in range(len(num_as_sting)):
        digit = int(num_as_sting[0])
        if digit % number == 0:
            magic = True
        else:
            macig = False
        digit = int(num_as_sting[1])
        if digit % number == 0:
            magic = True
        else:
            macig = False
        digit = int(num_as_sting[2])
        if digit % number == 0:
            magic = True
        else:
            macig = False
        digit = int(num_as_sting[3])
        if digit % number == 0:
            magic = True
        else:
            macig = False
            if macig == True:
                print(num , end = ' ')


    print(num, end = ' ')
