start = int(input())
end = int(input())

for num in range(start, end + 1):
    num_as_string = str(num)
    even_sum = 0
    odd_sum = 0
    for i in range(len(num_as_string)):
        digit = int(num_as_string[i])
        if (i + 1) % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum == odd_sum:
        print(num , end= ' ')

