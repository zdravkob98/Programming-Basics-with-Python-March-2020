import sys
goal = 10000
goal_for_day = False

while goal > 0:
    steps = input()
    if steps != 'Going home':

        goal -= int(steps)
    else:
        goal -= int(input())
        if goal> 0 :
            goal_for_day = False
        sys.exit()
if goal_for_day == False:
    print(f'{(goal)} more steps to reach goal.')
else:
    print('Goal reached! Good job!')