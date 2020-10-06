type_flowers = input()
count_flowers = int(input())
budget = int(input())

#Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";

discount = 0
price = 0
price_up = 0

if type_flowers == 'Roses' :
    price = 5
    if  count_flowers > 80:
        discount = 10
elif type_flowers == 'Dahlias' :
    price = 3.80
    if count_flowers > 90:
        discount = 15
elif type_flowers == 'Tulips' :
    price = 2.80
    if count_flowers > 80:
        discount = 15
elif type_flowers == 'Narcissus' :
    price = 3
    if count_flowers < 120:
        price_up = 15
elif type_flowers == 'Gladiolus' :
    price = 2.50
    if count_flowers < 80:
        price_up = 20

total = (count_flowers * price)
total = total - ((total * discount) / 100)
total = total + ((total * price_up) / 100)

#•	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
#•	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".

if budget >= total:
    print(f'Hey, you have a great garden with {count_flowers} {type_flowers} and {budget - total:.2f} leva left.')
else:
    print(f'Not enough money, you need {total - budget:.2f} leva more.')