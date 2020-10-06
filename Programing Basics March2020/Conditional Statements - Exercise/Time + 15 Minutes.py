start_hour = int(input())
start_minutes = int(input())

time_in_minutes = start_hour * 60 + start_minutes
time_plus_15_min = time_in_minutes + 15

final_hour = time_plus_15_min // 60
final_min = time_plus_15_min % 60

if final_hour > 23:
    final_hour = final_hour - 24

if final_min < 10:
    print(f'{final_hour}:0{final_min}')
else:
    print(f'{final_hour}:{final_min}')