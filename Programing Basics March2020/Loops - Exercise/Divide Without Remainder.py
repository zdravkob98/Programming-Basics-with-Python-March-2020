n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0

for i in range(n):
    maimuna=int(input())

    if maimuna % 2 == 0 :
        p1_count += 1
    if maimuna % 3 == 0 :
        p2_count += 1
    if maimuna % 4 == 0 :
        p3_count += 1

percentage_p1 = p1_count / n * 100
percentage_p2 = p2_count / n * 100
percentage_p3 = p3_count / n * 100

print(f'{percentage_p1:.2f}%')
print(f'{percentage_p2:.2f}%')
print(f'{percentage_p3:.2f}%')
