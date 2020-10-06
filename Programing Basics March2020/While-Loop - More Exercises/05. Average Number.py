n = int(input())


consecutive_number = 0
sum = 0

while consecutive_number != n :
    consecutive_number += 1
    line = int(input())
    sum += line
print(f'{sum / consecutive_number:.2f}')
