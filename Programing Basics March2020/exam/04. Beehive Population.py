import math
bee_population = int(input())
years = int(input())

for year in range(1, years +1):

    if year % 5 == 0:
        new_bee = math.floor(bee_population / 10) * 2
        bee_population += new_bee
        missing = math.floor(bee_population / 50) * 5
        bee_population -= missing
        died_bee = math.floor(bee_population / 20) * 2
        bee_population -= died_bee


    else:
        new_bee = math.floor(bee_population / 10) * 2
        bee_population += new_bee
        died_bee = math.floor(bee_population / 20) * 2
        bee_population -= died_bee



print(f"Beehive population: {bee_population}")


