import sys
steps = 10000

while steps > 0:
    el = input()
    if el != 'Going home':
        steps -= int(el)
    else:
        steps -= int(input())
        if steps > 0:
            print(f'{abs(steps)} more steps to reach goal.')
            sys.exit()
print('Goal reached! Good job!')