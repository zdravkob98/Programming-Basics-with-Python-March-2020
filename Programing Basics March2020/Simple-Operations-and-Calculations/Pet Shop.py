dogs_count = int(input())
other_animals_count = int(input())
price_per_dog = 2.5
price_per_animal = 4


dogs_total_price =dogs_count * price_per_dog
animal_total_price =other_animals_count*price_per_animal
total_price= dogs_total_price + animal_total_price
print(f'{total_price:.2f} lv.')