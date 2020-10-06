moves = int(input())
first = 0
second = 0
third = 0
four = 0
five = 0
invalid = 0
all = 0
for i in range(1 , moves + 1):
    number = int(input())
    if number > 50 or number < 0:
        all = all / 2
        invalid += 1
    elif 0 <= number <= 9 :
        all += (number / 100) * 20
        first += 1
    elif 10 <= number <= 19 :
        second += 1
        all += (number / 100) * 30
    elif 20 <= number <= 29 :
        third += 1
        all += (number / 100) * 40
    elif 30 <= number <= 39 :
        four += 1
        all += 50
    elif 40 <= number <= 50 :
        five += 1
        all += 100

print(f'{all:.2f}')
print(f'From 0 to 9: {first / moves * 100:.2f}%')
print(f'From 10 to 19: {second/moves * 100:.2f}%')
print(f'From 20 to 29: {third/moves * 100:.2f}%')
print(f'From 30 to 39: {four/moves * 100:.2f}%')
print(f'From 40 to 50: {five/moves * 100:.2f}%')
print(f'Invalid numbers: {invalid/moves * 100:.2f}%')






