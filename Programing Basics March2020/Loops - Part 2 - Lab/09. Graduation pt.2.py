name = input()
grades = 1
average_score = 0
failed_grades = 0
while grades <= 12 :
    score = float(input())
    if score >= 4:
        grades += 1
        average_score += score
    elif score < 4:
        failed_grades += 1

        break
average_score /= 12
if failed_grades == 1 :
    print(f'{name} has been excluded at {grades} grade')
else:
    print(f'{name} graduated. Average grade: {average_score:.2f}')
