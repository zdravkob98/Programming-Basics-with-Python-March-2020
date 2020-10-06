bottles = int(input())
quantity_ml = bottles * 750

time = 0
tendjari = 0
chinii = 0

line = input()

while line != 'End':
    line = int(line)
    time += 1
    if time % 3 == 0:
        tendjari += line
        line *= 15
        quantity_ml -= line

    else:
        chinii += line
        line *= 5
        quantity_ml -= line
    if quantity_ml < 0:
        print(f"Not enough detergent, {abs(quantity_ml)} ml. more necessary!")
        break
    line = input()

if line == 'End':
    if quantity_ml >= 0:
        print("Detergent was enough!")
        print(f"{chinii} dishes and {tendjari} pots were washed.")
        print(f'Leftover detergent {quantity_ml} ml.')
    else:
        print(f"Not enough detergent, {abs(quantity_ml)} ml. more necessary!")

