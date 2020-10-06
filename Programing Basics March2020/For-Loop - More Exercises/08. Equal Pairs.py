n = int(input())
sum = 0
sum2 = 0

max_diff = 0

for _ in range(n):
    a = int(input())
    b = int(input())
    if sum == 0 :
        sum = a + b
    else:
        sum2 = a + b

        if sum == sum2:
            sum = 0
        else:
            diff = abs(sum - sum2)
            if max_diff < diff:
                max_diff = diff
                sum = 0

if sum == sum2:
    print(f'Yes, value={sum}')
else:
    print(f'No, maxdiff={max_diff}')

