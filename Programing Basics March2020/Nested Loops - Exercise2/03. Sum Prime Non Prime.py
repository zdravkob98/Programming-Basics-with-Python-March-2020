line = input()

prime_sum = 0
non_prime_sum = 0

while line != 'stop':
    number = int(line)
    help = True


    if number < 0:
        print('Number is negative.')
    else:
        for i in range(2, number):
            if number % i == 0:
                non_prime_sum += number
                help = False
                break
        if help == True:
            prime_sum += number







    line = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f'Sum of all non prime numbers is: {non_prime_sum}')

