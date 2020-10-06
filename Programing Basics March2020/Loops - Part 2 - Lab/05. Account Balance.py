n = int(input())
i = 0

balance = 0

while i < n:
    money = float(input())
    if money < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {money:.2f}')
    balance += money
    i += 1
print(f'Total: {balance:.2f}')