trip_price = float(input())
count_puzzles = int(input())
count_toys = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

count_sells_toys = count_puzzles + count_toys + count_bears + count_minions + count_trucks

price_per_puzzle = 2.60
price_per_toys = 3
price_per_bear = 4.10
price_per_minion = 8.20
price_per_truck = 2

total_money = count_puzzles * price_per_puzzle + count_toys * price_per_toys + count_bears * price_per_bear + count_minions * price_per_minion + count_trucks * price_per_truck

if count_sells_toys >= 50 :
    total_money = total_money * 0.75

total_money = total_money * 0.90

if total_money >= trip_price :
    print(f"Yes! {total_money - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total_money:.2f} lv needed.")





