import sys
n = int(input())
i = 0

min_num = sys.maxsize

while i < n :
    number = int(input())
    if number < min_num:
        min_num = number
    i += 1
print(min_num)