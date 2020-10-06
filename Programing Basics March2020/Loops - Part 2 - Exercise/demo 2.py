goal = 10000

goal_per_day = False
more = 0

while True:
    steps = input()
    if steps == int(input()):
        more += int(steps)


    if more >= goal:
        goal_per_day = True
        break

    elif steps == 'Going home':
        steps = input()
        more += int(steps)
        if more >= goal:
            goal_per_day = True
            break
        else:
            goal_per_day = False
            break
if goal_per_day == True:
    print("Goal reached! Good job!")
elif goal_per_day == False:
    print(f"{goal - more} more steps to reach goal.")