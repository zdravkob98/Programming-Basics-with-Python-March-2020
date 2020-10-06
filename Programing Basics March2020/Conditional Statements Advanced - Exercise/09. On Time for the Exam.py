hour_exam = int(input())
min_exam = int(input())
hour_of_arrival = int(input())
min_of_arrival = int(input())

exam = f'{hour_exam}:{min_exam}'
arrival = f'{hour_of_arrival}:{min_of_arrival}'
num = 30


if exam == arrival:
    print('On time')
elif exam > arrival and min_exam - min_of_arrival < num :
    print('On time')
   #print(f'{min_exam - min_of_arrival} minutes before the start')