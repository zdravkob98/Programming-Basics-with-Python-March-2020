mount = int(input())
Water = 20
Internet = 15


electricity_average = 0
water_average = 0
internet_average = 0
other_average = 0


for i in range(1, mount +1):
    Electricity = float(input())
    Other = ((Water + Electricity + Internet) * 0.20) + Water + Electricity + Internet

    electricity_average += Electricity
    water_average += Water
    internet_average += Internet
    other_average += Other





print(f'Electricity: {electricity_average:.2f} lv')
print(f'Water: {water_average:.2f} lv')
print(f'Internet: {internet_average:.2f} lv')
print(f'Other: {other_average:.2f} lv')
print(f'Average: {(electricity_average + water_average + internet_average + other_average) / mount:.2f} lv')
