count_days = int(input())
count_food = float(input())

cookies = 0
total_food = 0
dog_food = 0
cat_food = 0

for i in range(1, count_days +1):
    dog = int(input())
    cat = int(input())
    if i % 3 == 0:
        cookies += (dog + cat) * 0.10
    total_food += dog + cat
    dog_food += dog
    cat_food += cat



print(f'Total eaten biscuits: {round(cookies)}gr.')
print(f'{(total_food / count_food) * 100:.2f}% of the food has been eaten.')
print(f'{dog_food / total_food * 100:.2f}% eaten from the dog.')
print(f'{cat_food / total_food * 100:.2f}% eaten from the cat.')
