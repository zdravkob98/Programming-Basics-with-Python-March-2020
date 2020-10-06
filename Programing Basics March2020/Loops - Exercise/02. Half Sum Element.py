import sys
n = int(input())

max_num = -sys.maxsize
sum_number = 0

for i in range(n):
    number = int(input())
    sum_number += number

    if number >= max_num:
        max_num = number

sum_number -= max_num

#print(max_num)
#print(sum_number)

if sum_number == max_num:
    print(f'Yes')
    print(f'Sum = {max_num} ')
else:
    print(f'No')
    print(f'Diff = {abs(max_num - sum_number)}')