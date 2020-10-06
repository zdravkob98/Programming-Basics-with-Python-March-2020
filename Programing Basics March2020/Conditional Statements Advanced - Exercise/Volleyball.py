import math
year = input()
p = int(input())
h = int(input())

weekends = 48

weekends_in_sofia = weekends - h
weekends_day_play_sofia = weekends_in_sofia * 0.75
play_in_borntown = h
happy_days = p * 0.66

total_play_days = weekends_day_play_sofia + happy_days + play_in_borntown

if year == 'leap':
    (total_play_days) = total_play_days + ((total_play_days * 15) / 100 )
else:
    total_play_days = total_play_days

print(math.floor(total_play_days))