import math
count_people = int(input())
tax = float(input())
price_chaise_lounge = float(input())
price_for_umbrella = float(input())

total_taxes = count_people * tax
using_umbrella = math.ceil(count_people / 2) * price_for_umbrella
using_chaise_lounge = math.ceil(count_people * 0.75) * price_chaise_lounge


total = total_taxes + using_umbrella + using_chaise_lounge

print(f'{total:.2f} lv.')