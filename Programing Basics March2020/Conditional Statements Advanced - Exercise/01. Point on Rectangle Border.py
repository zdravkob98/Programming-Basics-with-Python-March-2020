x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

#•	x съвпада с x1 или x2 и същевременно y е между y1 и y2;
#•	y съвпада с y1 или y2 и същевременно x е между x1 и x2.

first_condition =(x == x1 or x == x2) and (y1 < y < y2)
second_condition = (y == y1 or y == y2) and (x1 < x < x2)

if (x == x1 or x == x2) and (y1 <= y <= y2):
    print('Border')
elif (y == y1 or y == y2) and (x1 <= x <= x2):
    print('Border')
else:
    print("Inside / Outside")