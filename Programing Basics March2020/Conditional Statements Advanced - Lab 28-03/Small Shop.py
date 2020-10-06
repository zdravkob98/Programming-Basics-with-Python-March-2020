product = input()
town = input()
quantity = float(input())

price = 0

if product == 'coffee':
    if town == 'Sofia':
        price = 0.50
    elif town == 'Plovdiv':
        price = 0.40
    else :
        price = 0.45
elif product == 'water':
    if town == 'Sofia':
        price = 0.80
    elif town == 'Plovdiv':
        price = 0.70
    else :
        price = 0.70
elif product == 'beer':
    if town == 'Sofia':
        price = 1.20
    elif town == 'Plovdiv':
        price = 1.15
    else :
        price = 1.10
elif product == 'sweets':
    if town == 'Sofia':
        price = 1.45
    elif town == 'Plovdiv':
        price = 1.30
    else :
        price = 1.35
elif product == 'peanuts':
    if town == 'Sofia':
        price = 1.60
    elif town == 'Plovdiv':
        price = 1.50
    else :
        price = 1.55


total_price = price * quantity
print(total_price)

