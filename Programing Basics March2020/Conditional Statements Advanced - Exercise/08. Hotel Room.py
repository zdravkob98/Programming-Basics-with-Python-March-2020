mouth = input()
count_night = int(input())

type_room = 'Studio'
type_room2 = 'Apartment'
price = 0
price2 = 0
discount = 0
dis_apart = 0

if mouth == 'May' or mouth == 'October':
    type_room == 'Studio'
    price = 50
    type_room2 == 'Apartment'
    price2 = 65
elif mouth == 'June' or mouth == 'September':
    type_room == 'Studio'
    price = 75.20
    type_room2 == 'Apartment'
    price2 = 68.70
elif mouth == 'July' or mouth == 'August':
    type_room == 'Studio'
    price = 76
    type_room2 == 'Apartment'
    price2 = 77


if type_room == 'Studio' and 7 < count_night < 14 and mouth == 'May' or mouth == 'October':
    discount = 5
elif type_room == 'Studio' and count_night >= 14 and mouth == 'May' or mouth == 'October':
    discount = 30
elif type_room == 'Studio' and count_night >= 14 and mouth == 'June' or mouth == 'September':
    discount = 20

if count_night > 14:
    if type_room2 == 'Apartment':
        dis_apart = 10

total = price * count_night
total = total - ((total * discount) / 100)

total2 = price2 * count_night
total2 = total2 - ((total2 * dis_apart) / 100)

print(f'Apartment: {total2:.2f} lv. ')
print(f'Studio: {total:.2f} lv. ')
