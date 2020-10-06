import sys
n = int(input())
i = 0

max_num = -sys.maxsize

while i < n :
    number = int(input())
    if number > max_num:
        max_num = number
    i += 1
print(max_num)