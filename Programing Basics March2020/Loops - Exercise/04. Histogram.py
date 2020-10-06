n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(1 , n + 1 ):
    number = int(input())
    if number < 200 :
        p1_count += 1
    elif 200 <= number <= 399:
        p2_count += 1
    elif 400 <= number <= 599:
        p3_count += 1
    elif 600 <= number <= 799:
        p4_count += 1
    else:
        p5_count += 1

percentage1 = p1_count / n * 100
percentage2 = p2_count / n * 100
percentage3 = p3_count / n * 100
percentage4 = p4_count / n * 100
percentage5 = p5_count / n * 100


print(f'{percentage1:.2f}%')
print(f'{percentage2:.2f}%')
print(f'{percentage3:.2f}%')
print(f'{percentage4:.2f}%')
print(f'{percentage5:.2f}%')
