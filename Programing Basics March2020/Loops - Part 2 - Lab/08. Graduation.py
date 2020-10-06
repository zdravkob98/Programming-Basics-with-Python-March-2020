name = input()
grades = 1
average_score = 0
while grades <= 12 :
    score = float(input())
    if score >= 4:
        grades += 1
        average_score += score

average_score /= 12
print(f'{name} graduated. Average grade: {average_score:.2f}')
