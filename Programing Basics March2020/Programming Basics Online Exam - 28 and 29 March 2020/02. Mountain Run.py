import math
recor_in_second = float(input())
distance_in_meters = float(input())
second_for_meter = float(input())

delay = math.floor(distance_in_meters / 50)
delay *= 30

total = distance_in_meters * second_for_meter + delay
if total < recor_in_second:
    print(f'Yes! The new record is {total:.2f} seconds.')
else:
    print(f'No! He was {total - recor_in_second:.2f} seconds slower.')