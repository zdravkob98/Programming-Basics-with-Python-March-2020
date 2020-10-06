fruit = input()
size_of_packet = input()
count_order_packet = int(input())

price = 0



if fruit == 'Watermelon':
    if size_of_packet == 'small':
        price = 2 * 56
    else:
        price = 5 * 28.70
elif fruit == 'Mango':
    if size_of_packet == 'small':
        price = 2 * 36.66
    else:
        price = 5 * 19.60
elif fruit == 'Pineapple':
    if size_of_packet == 'small':
        price = 2 * 42.10
    else:
        price = 5 * 24.80
else:
    if size_of_packet == 'small':
        price = 2 * 20
    else:
        price = 5 * 15.20

total = price * count_order_packet

if 400 <= total <= 1000 :
    print(f'{total * 0.85:.2f} lv.')
elif 1000 < total :
    print(f'{total * 0.50:.2f} lv.')
else:
    print(f'{total:.2f} lv.')


