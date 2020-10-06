type_cruise = input()
type_cabin = input()
count_night = int(input())

price = 0

if type_cruise == "Mediterranean":
    if type_cabin == "standard cabin":
        price = 27.50 * 4
    elif type_cabin == "cabin with balcony":
        price = 30.20 * 4
    elif type_cabin == "apartment":
            price = 40.50 * 4

elif type_cruise == "Adriatic":
    if type_cabin == "standard cabin":
        price = 22.99 * 4
    elif type_cabin == "cabin with balcony":
        price = 25.00 * 4
    elif type_cabin == "apartment":
            price = 34.99 * 4

elif type_cruise == "Aegean":
    if type_cabin == "standard cabin":
        price = 23.00 * 4
    elif type_cabin == "cabin with balcony":
        price = 26.60 * 4
    elif type_cabin == "apartment":
            price = 39.80 * 4

total = price * count_night

if count_night > 7 :
    discount = total * 0.25
    total -= discount

print(f"Annie's holiday in the {type_cruise} sea costs {total:.2f} lv.")


