town = input()
sales = float(input())

percentage = 0

if 0 <= sales <= 500:
    if town == 'Sofia':
        percentage = 5
    elif town == 'Varna':
        percentage = 4.5
    elif town == 'Plovdiv':
        percentage = 5.5
elif 500 < sales <= 1000:
    if town == 'Sofia':
        percentage = 7
    elif town == "Varna":
        percentage = 7.5
    elif town == 'Plovdiv':
        percentage = 8
elif 1000 < sales <= 10000:
    if town == 'Sofia':
        percentage = 8
    elif town == "Varna":
        percentage = 10
    elif town == 'Plovdiv':
        percentage = 12
elif sales > 10000:
    if town == 'Sofia':
        percentage = 12
    elif town == "Varna":
        percentage = 13
    elif town == 'Plovdiv':
        percentage = 14.5


total = (sales / 100 ) * percentage

if percentage == 0:
    print('error')
else:
    print(f'{total:.2f}')
