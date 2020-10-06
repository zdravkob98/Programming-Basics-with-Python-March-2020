start = int(input())
end = int(input())
number = int(input())

combination = 0

flag = True

for n1 in range(start, end +1):
    for n2 in range(start, end+1):
        combination += 1
        if n1 + n2 == number:
            print(f'Combination N:{combination} ({n1} + {n2} = {n1 + n2})')
            flag = False
            break

    if flag == False:
        break
if flag == True:
    print(f'{combination} combinations - neither equals {number}')



