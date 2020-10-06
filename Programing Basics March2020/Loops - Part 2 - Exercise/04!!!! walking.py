goal = 10000

line = input()

while line != 'Going home':
    line = int(line)

    goal -= line
    if goal <= 0:
        print('Goal reached! Good job!')
        break


    line = input()

if line == 'Going home':
    line = int(input())
    goal -= line
    if goal <= 0 :
        print('Goal reached! Good job!')
    else:
        print(f'{goal} more steps to reach goal.')