import math
bee = int(input())
flowers = int(input())

honey = bee * flowers * 0.21
count_Honeycombs = math.floor(honey / 100)

print(f"{count_Honeycombs} honeycombs filled.")
the_rest = honey -(count_Honeycombs * 100)
print(f"{the_rest:.2f} grams of honey left.")
