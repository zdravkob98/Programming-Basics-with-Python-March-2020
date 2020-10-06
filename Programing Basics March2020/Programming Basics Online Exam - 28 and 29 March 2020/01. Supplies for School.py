#•	Пакет химикали - 5.80 лв
#•	Пакет маркери - 7.20 лв
#•	Препарат - 1.20 лв (за литър)

count_pens = int(input())
count_markers = int(input())
preparation = float(input())
percentage = int(input())

pens = count_pens * 5.80
markers = count_markers * 7.20
preparat = preparation * 1.20

total = pens + markers + preparat
help = total - (total / 100 * percentage)
print(f'{help:.3f}')