count_days = int(input())
count_bakers = int(input())
count_cakes = int(input())
count_waffles = int(input())
count_pancakes = int(input())

price_cakes = 45
price_waffles = 5.80
price_pancakes = 3.20

total_cakes = count_cakes * price_cakes
total_waffles = count_waffles * price_waffles
total_pancakes = count_pancakes * price_pancakes

total_price_per_day = (total_cakes + total_waffles + total_pancakes) * count_bakers
total_price_per_company = total_price_per_day * count_days
total_price_without_coast = total_price_per_company - total_price_per_company / 8

print(f'{total_price_without_coast:.2f}')

