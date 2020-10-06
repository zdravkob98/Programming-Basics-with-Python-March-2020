flower = input()
count_flowers = int(input())
season = input()

total_honey = 0

if flower == 'Sunflower':
    if season == 'Spring':
        total_honey += 10
    elif season == 'Summer':
        total_honey += 8
    elif season == 'Autumn':
        total_honey += 12
elif flower == 'Daisy':
    if season == 'Spring':
        total_honey += 12
    elif season == 'Summer':
        total_honey += 8
    elif season == 'Autumn':
        total_honey += 6
elif flower == 'Lavender':
    if season == 'Spring':
        total_honey += 12
    elif season == 'Summer':
        total_honey += 8
    elif season == 'Autumn':
        total_honey += 6
elif flower == 'Mint':
    if season == 'Spring':
        total_honey += 10
    elif season == 'Summer':
        total_honey += 12
    elif season == 'Autumn':
        total_honey += 6

total_honey = total_honey * count_flowers
if season == 'Summer':
    total_honey *= 1.10
elif season == 'Autumn':
    total_honey *= 0.95
elif season == 'Spring' and flower == 'Daisy' or flower == 'Mint':
    total_honey *= 1.10
print(f"Total honey harvested: {total_honey:.2f}")