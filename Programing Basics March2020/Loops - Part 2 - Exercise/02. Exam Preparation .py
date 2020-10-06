failed_treshhold = int(input())

tasks = 0
solved_problems_count = 0
grade_sum = 0
last_problem = ''
has_failed = True

while solved_problems_count < failed_treshhold:
    name_problem = input()
    if name_problem == 'Enough':
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        solved_problems_count += 1

    grade_sum += grade
    tasks += 1
    last_problem = name_problem
if has_failed:
    print(f'You need a break, {failed_treshhold} poor grades.')
else:
    print(f"Average score: {grade_sum/tasks:.2f}")
    print(f"Number of problems: {tasks}")
    print(f"Last problem: {last_problem}")
