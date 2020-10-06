stadium_capacity = int(input())
people = int(input())

A = 0
B = 0
V = 0
G = 0


for i in range ( 1 , people + 1):
    sectors = input()
    if sectors == 'A':
        A += 1
    elif sectors == 'B':
        B += 1
    elif sectors == 'V':
        V += 1
    elif sectors == 'G':
        G += 1

print(f'{A / people * 100:.2f}%')
print(f'{B / people * 100:.2f}%')
print(f'{V / people * 100:.2f}%')
print(f'{G / people * 100:.2f}%')
print(f'{people / stadium_capacity * 100:.2f}%')


