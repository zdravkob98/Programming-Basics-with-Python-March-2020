width = int(input())
length = int(input())
height = int(input())

packet = 0

space = width * length * height

new = input()

while new != 'Done':
    pack = int(new)
    packet += pack
    if space < packet:
        break
    new = input()
if space < packet:
    print(f'No more free space! You need {packet - space} Cubic meters more.')
else:
    print(f'{space - packet} Cubic meters left.')