money_needed = int(input())

people_with_card = 0
people_with_cash = 0
count_pay_with_cash = 0
count_pay_with_card = 0
income = 0
logic = 1
payments = 0

line = input()

while line != 'End':
    line = int(line)

    if logic == 1 :
        if line > 100:
            logic += 1
            print('Error in transaction!')
        else:
            count_pay_with_cash += line
            people_with_cash += 1
            income += line
            logic += 1
            payments += 1
            print('Product sold!')
    elif logic == 2 :
        if line < 10 :
            logic -= 1
            print('Error in transaction!')
        else:
            count_pay_with_card += line
            people_with_card += 1
            income += line
            logic -= 1
            payments += 1
            print('Product sold!')
    if income >= money_needed :
        print(f'Average CS: {count_pay_with_cash / people_with_cash:.2f}')
        print(f'Average CC: {count_pay_with_card / people_with_card:.2f}')
        break
    line = input()

if line == 'End':
    print('Failed to collect required money for charity.')