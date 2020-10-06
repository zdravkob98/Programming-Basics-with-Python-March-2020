capacity = float(input())
count_suitcases = 0
full = False
couter = 0
line = input()

while line != 'End':
    couter += 1
    suitcases = float(line)

    if couter == 3:
        suitcases *= 1.10

    if capacity < suitcases:
        print("No more space!")
        print(f"Statistic: {count_suitcases} suitcases loaded.")
        full = True
        break
    else:
        capacity -= suitcases
        count_suitcases += 1
    line = input()

if full == False:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {count_suitcases} suitcases loaded.")
