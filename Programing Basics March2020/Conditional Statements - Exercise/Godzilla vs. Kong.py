budget = float(input())
people = int(input())
price_for_clothe = float(input())

decor = budget * 0.10

#print(decor)

if people >= 150 :
    price_for_clothe = price_for_clothe * 0.90

total_money_for_people = people * price_for_clothe

#print(total_money_for_people)

total_money = total_money_for_people + decor
#print(total_money)

#print(budget)

if budget > total_money:
    print("Action!")
    print(f"Wingard starts filming with {budget-total_money:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_money - budget:.2f} leva more.")

