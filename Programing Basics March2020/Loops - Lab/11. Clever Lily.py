n = int(input())
price_for_machine = float(input())
price_per_toy = int(input())

saving = 0
toys = 0

for i in range(1 , n + 1):
    if i % 2 == 0:
        saving += i * 5
        saving -= 1
    else:
        toys += 1

total_price_toys = price_per_toy * toys

saving += total_price_toys


if saving >= price_for_machine:
    money_left = saving - price_for_machine
    print(f'Yes! {money_left:.2f}')
else:
    money_need = price_for_machine - saving
    print(f'No! {money_need:.2f}')

