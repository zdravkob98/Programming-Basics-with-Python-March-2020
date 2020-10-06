budget = int(input())
season = input()
count_fishermen = int(input())



price = 0
discount = 0
discount2 = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer':
    price = 4200
elif season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if count_fishermen <= 6:
    discount = 10
elif 7 <= count_fishermen <= 11 :
    discount = 15
elif count_fishermen >= 12 :
    discount = 25

if count_fishermen % 2 == 0 and season != 'Autumn':
    discount2 = 5

total = price - ((price * discount) / 100)
total = total - ((total * discount2) / 100)

if budget >= total:
    print(f"Yes! You have {budget - total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva.")


