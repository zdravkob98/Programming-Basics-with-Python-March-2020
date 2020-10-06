groups = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
count_people = 0

for groups in range(1, groups +1):
    line = int(input())
    count_people += line
    if line <= 5:
        musala += line
    elif 6 <= line <= 12:
        monblan += line
    elif 13 <= line <= 25:
        kilimandjaro += line
    elif 26 <= line <= 40:
        k2 += line
    elif 41 <= line :
        everest += line
print(f'{musala / count_people * 100:.2f}%')
print(f'{monblan / count_people * 100:.2f}%')
print(f'{kilimandjaro / count_people * 100:.2f}%')
print(f'{k2 / count_people * 100:.2f}%')
print(f'{everest / count_people * 100:.2f}%')


