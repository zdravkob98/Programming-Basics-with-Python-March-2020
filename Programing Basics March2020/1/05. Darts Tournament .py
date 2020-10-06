total_points = int(input())

trys = 0

while total_points != 0:
    trys += 1
    sector = input()

    if sector == 'bullseye':
        print(f"Congratulations! You won the game with a bullseye in {trys} moves!")
        break

    points = int(input())

    if sector == 'number section':
        total_points -= points
    elif sector == 'double ring':
        points *= 2
        total_points -= points
    elif sector == 'triple ring':
        points *= 3
        total_points -= points

    if total_points == 0:
        print(f"Congratulations! You won the game in {trys} moves!")
        break
    if total_points < 0:
        print(f"Sorry, you lost. Score difference: {abs(total_points)}.")
        break






