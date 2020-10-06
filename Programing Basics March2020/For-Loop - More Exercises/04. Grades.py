count_student = int(input())
slab = 0
sreden = 0
dobur = 0
nai_dobrite = 0
average = 0


for i in range( 1 , count_student +1):
    grade = float(input())
    average += grade
    if 2.00 <= grade <= 2.99:
        slab += 1
    elif 3.00 <= grade <= 3.99:
        sreden += 1
    elif 4.00 <= grade <= 4.99:
        dobur += 1
    else:
        nai_dobrite += 1

print(f'Top students: {nai_dobrite / count_student * 100:.2f}%')
print(f'Between 4.00 and 4.99: {dobur / count_student * 100:.2f}%')
print(f'Between 3.00 and 3.99: {sreden / count_student * 100:.2f}%')
print(f'Fail: {slab / count_student * 100:.2f}%')
print(f'Average: {average / count_student:.2f}')