screaming_type = input()
count_rows = int(input())
count_col = int(input())

place = count_col * count_rows

price = 0
if screaming_type == 'Premiere':
     price = 12
elif screaming_type == 'Normal':
    price = 7.5
elif screaming_type == 'Discount':
    price =  5

total = place * price

print(f'{total:.2f} leva')