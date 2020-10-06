width = int(input())
length = int(input())

cake = width * length

line = input()
while line != 'STOP' :
    line = int(line)

    cake -= line
    if cake < 0 :
        print(f"No more cake left! You need {abs(cake)} pieces more.")
        break

    line = input()
if line == 'STOP':
    print(f"{cake} pieces are left." )