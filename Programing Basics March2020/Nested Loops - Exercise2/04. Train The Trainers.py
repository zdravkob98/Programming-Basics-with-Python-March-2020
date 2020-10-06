jury = int(input())

line = input()
sum = 0
help = 0

while line != 'Finish':
    presentation = line
    grades_sum = 0

    for i in range(1, jury + 1):
        grades = float(input())
        grades_sum += grades
        sum += grades
        help +=1
    print(f'{presentation} - {grades_sum / jury:.2f}.')



    line = input()
print(f"Student's final assessment is {sum /help:.2f}." )
