count_table = int(input())
length_table = float(input())
width_table = float(input())

table_cloth_area = count_table * (length_table + 0.30 * 2) * (width_table + 0.30 * 2)
table_square_area = count_table * pow(length_table /2, 2)

dollars_total = table_cloth_area * 7 + table_square_area * 9
bgn_total = dollars_total * 1.85

print(f'{dollars_total:.2f} USD')
print(f'{bgn_total:.2f} BGN')
