count_days = int(input())

total_money = 0
total_win = 0
total_lose = 0
for day in range(1, count_days +1):
    lose = 0
    win = 0
    count_money_per_day = 0

    line = input()

    while line != 'Finish':
        games = line
        win_or_lose = input()
        if win_or_lose == 'win':
            win += 1
            count_money_per_day += 20
            total_win += 1
        else:
            lose += 1
            total_lose += 1
        line = input()
    if win > lose :
        count_money_per_day *= 1.10
    total_money += count_money_per_day
if total_win > total_lose:
    total_money *= 1.20
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')
