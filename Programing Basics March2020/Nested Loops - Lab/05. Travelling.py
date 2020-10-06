destination = input()

while destination != 'End':
    budget = int(input())
    saving = 0
    while saving < budget:
        line = int(input())
        saving += line

    print(f'Going to {destination}!')

    destination = input()

