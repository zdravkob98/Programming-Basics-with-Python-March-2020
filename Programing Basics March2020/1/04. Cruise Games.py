import math
name = input()
games = int(input())

sum_points = 0

volleyball_point = 0
v_games = 0
tennis_point = 0
t_games = 0
bardminton = 0
b_games = 0


for i in range(games):
    game_name = input()
    points = int(input())

    if game_name == "volleyball":
        points *= 1.07
        sum_points += points
        volleyball_point += points
        v_games += 1



    elif game_name == "tennis":
        points *= 1.05
        sum_points += points
        tennis_point += points
        t_games += 1

    elif game_name == 'badminton':
        points *= 1.02
        sum_points += points
        bardminton += points
        b_games += 1

a = math.floor(volleyball_point / v_games)
b = math.floor(tennis_point / t_games)
c = math.floor(bardminton / b_games)

if  a >= 75 and b >= 75 and c >= 75:
    print(f"Congratulations, {name}! You won the cruise games with {math.floor(sum_points)} points.")
else:
    print(f"Sorry, {name}, you lost. Your points are only {math.floor(sum_points)}.")

