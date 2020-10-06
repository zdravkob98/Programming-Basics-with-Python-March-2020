days = int(input())
rooms = input()
grade = input()

days = days - 1
price = 0
discount = 0

if days < 10 :
    if rooms == "room for one person":
        price = 18
        discount = 0
    elif rooms =="apartment":
        price = 25
        discount = 30
    elif rooms == "president apartment":
        price = 35
        discount = 10
elif 10 <= days <= 15 :
    if rooms == "room for one person":
        price = 18
        discount = 0
    elif rooms == "apartment":
        price = 25
        discount = 35
    elif rooms == "president apartment":
        price = 35
        discount = 15
elif days > 15:
    if rooms == "room for one person":
        price = 18
        discount = 0
    elif rooms == "apartment":
        price = 25
        discount = 50
    elif rooms == "president apartment":
        price = 35
        discount = 20

total = ((price * days) / 100) * discount
final_price = price * days - total


if grade == 'positive':
    final_price = final_price * 0.25 + final_price
elif grade == 'negative':
    final_price = final_price * 0.90


print(f'{final_price:.2f}')
