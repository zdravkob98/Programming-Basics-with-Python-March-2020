count_bee = int(input())
health_bear = int(input())
attack_power_bear = int(input())

war = True

while war != False:
    count_bee -= attack_power_bear
    health_bear -= count_bee * 5
    if health_bear <= 0:
        print(f'Beehive won! Bees left {count_bee}.')
        war = False
        break
    elif count_bee < 100:
        if count_bee < 0:
            count_bee = 0
        print(f"The bear stole the honey! Bees left {count_bee}.")
        war = False
        break

