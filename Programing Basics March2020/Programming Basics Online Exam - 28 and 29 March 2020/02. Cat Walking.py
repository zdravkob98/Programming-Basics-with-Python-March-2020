min_walking = int(input())
count_walking = int(input())
calories = int(input())

calories_per_min = min_walking * 5
calories_for_all_day = calories_per_min * count_walking

if calories_for_all_day >= calories / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_for_all_day}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_for_all_day}.')