import sys
n = int(input())


OddSum = 0
OddMin = sys.maxsize
OddMax = -sys.maxsize
EvenSum = 0
EvenMin = sys.maxsize
EvenMax = -sys.maxsize


for i in range(1, n+1):
    number = float(input())
    if i % 2 == 0:
        EvenSum += number
        if number >= EvenMax:
            EvenMax = number
        if number <= EvenMin:
            EvenMin = number
    else:
        OddSum += number
        if number >= OddMax:
            OddMax = number
        if number <= OddMin:
            OddMin = number


print(f'OddSum={OddSum:.2f},')
if OddMin - sys.maxsize == 0 :
    print('OddMin=No,')
else:
    print(f'OddMin={OddMin:.2f},')
if OddMax + sys.maxsize == 0 :
    print('OddMax=No,')
else:
    print(f'OddMax={OddMax:.2f},')

print(f'EvenSum={EvenSum:.2f},')
if EvenMin - sys.maxsize == 0 :
    print('EvenMin=No,')
else:
    print(f'EvenMin={EvenMin:.2f},')
if EvenMax + sys.maxsize == 0 :
    print('EvenMax=No')
else:
    print(f'EvenMax={EvenMax:.2f}')
