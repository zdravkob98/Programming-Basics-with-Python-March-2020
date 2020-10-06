
length_hall_in_meters = float(input())
width_hall_in_meters = float(input())
side_wardrobe_in_meters = float(input())

size_of_hall_in_santimeters = (length_hall_in_meters * 100) * (width_hall_in_meters * 100)

#print(size_of_hall_in_santimeters)

size_of_wardrobe_in_santimeters = (side_wardrobe_in_meters * 100) * (side_wardrobe_in_meters * 100)
size_of_bench_in_santimeters = size_of_hall_in_santimeters / 10

free_place_in_santimeters = size_of_hall_in_santimeters - size_of_wardrobe_in_santimeters - size_of_bench_in_santimeters
free_place_for_dance = free_place_in_santimeters / (7000 + 40)

import math
print(math.floor(free_place_for_dance))

a=3
b=7
number = a - b

print(number)