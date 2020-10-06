count_goods = int(input())

count_tovari = 0
mikrobus = 0

kamion = 0

vlak = 0



for i in range(1, count_goods + 1):
    tonaj = int(input())
    count_tovari += tonaj
    if tonaj <= 3:
        mikrobus += tonaj
    elif 4 <= tonaj <= 11:
        kamion +=  tonaj
    else:
        vlak += tonaj
sredno = (kamion * 175 + mikrobus * 200 + vlak * 120) / count_tovari
print(f'{sredno:.2f}')
print(f'{mikrobus/count_tovari * 100:.2f}%')
print(f'{kamion/count_tovari * 100:.2f}%')
print(f'{vlak/count_tovari* 100:.2f}%')