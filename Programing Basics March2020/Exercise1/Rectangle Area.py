x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = abs(x1-x2)
width = abs(y1-y2)

area = length * width
perimetur= 2 * length + 2 * width

print(f'{area:.2f}')
print(f'{perimetur:.2f}')
