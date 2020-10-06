film = input()

sell = 0
student_t = 0
standard_t = 0
kid_t = 0

while film != 'Finish':
    free_place = int(input())
    ticket = input()
    full_seats = free_place

    while ticket != 'End' and free_place > 0:
        if ticket == 'student':
            student_t += 1
            sell += 1
            free_place -= 1
        elif ticket == 'standard':
            standard_t += 1
            sell += 1
            free_place -= 1
        else:
            kid_t += 1
            sell += 1
            free_place -= 1
        if free_place > 0:
            ticket = input()
    print(f'{film} - {(full_seats - free_place) / full_seats * 100:.2f}% full.')

    film = input()
print(f'Total tickets: {sell}')
print(f'{student_t / sell * 100:.2f}% student tickets.')
print(f'{standard_t / sell * 100:.2f}% standard tickets.')
print(f'{kid_t /sell * 100:.2f}% kids tickets.')


