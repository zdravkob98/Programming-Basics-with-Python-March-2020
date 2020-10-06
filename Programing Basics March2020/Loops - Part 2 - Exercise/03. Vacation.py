money_for_vocation = float(input())
money = float(input())

spending_days = 0
days = 0

while money < money_for_vocation and spending_days < 5:
    command = input()
    command_money = float(input())
    days += 1
    if command == 'spend':
        spending_days += 1
        money -= command_money
        if 0 > money:
            money = 0

    elif command == 'save':
        spending_days = 0
        money += command_money
if spending_days == 5:
    print('You can\'t save the money.')
    print(f'{days}')
elif money >= money_for_vocation:
    print(f'You saved the money for {days} days.')