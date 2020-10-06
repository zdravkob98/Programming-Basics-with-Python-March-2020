import math
figures = str(input())

if figures == 'square':
    side = float(input())
    area = side * side
    print(area)

elif figures == 'rectangle':
    width = float(input())
    height = float(input())
    area = width * height
    print(area)

elif figures == 'circle':
    radius = float(input())
    area = radius * radius * math.pi
    print(area)

elif figures == 'triangle' :
    length = float(input())
    height = float(input())
    area = length * height /2
    print(area)



