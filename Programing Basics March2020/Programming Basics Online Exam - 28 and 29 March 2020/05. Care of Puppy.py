count_food = int(input())
food_in_grams = count_food * 1000
count_eaten_food = 0
line = input()

while line != 'Adopted':
    eaten_food = int(line)
    count_eaten_food += eaten_food
    line = input()
if food_in_grams < count_eaten_food:
    print(f'Food is not enough. You need {count_eaten_food - food_in_grams} grams more. ')
else:
    print(f'Food is enough! Leftovers: {food_in_grams - count_eaten_food} grams.')
