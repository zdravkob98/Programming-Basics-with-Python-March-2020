money = float(input())
year = int(input())
year_old = 18

for i in range (1800 , year + 1):
    if i % 2 == 0 :
        money -= 12000
    elif i % 2 == 1:
        money -= 12000
        discount = year_old * 50
        money -= discount
    year_old += 1

if money >= 0 :
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    print(f'He will need {abs(money):.2f} dollars to survive. ')



