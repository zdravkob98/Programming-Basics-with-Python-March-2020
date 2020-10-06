budget = float(input())
season =input()

destination = ''
budget_for_vocation = 0
type = ''

if budget <= 100 :
    destination = 'Bulgaria'
    if season == 'summer' :
        type = 'Camp'
        budget_for_vocation = 30
    elif season == 'winter' :
        type = 'Hotel'
        budget_for_vocation = 70
elif budget <= 1000 :
    destination = 'Balkans'
    if season == 'summer' :
        type = 'Camp'
        budget_for_vocation = 40
    elif season == 'winter' :
        type = 'Hotel'
        budget_for_vocation = 80
elif budget > 1000 :
    destination = 'Europe'
    type = 'Hotel'
    budget_for_vocation = 90


total = ((budget * budget_for_vocation) / 100)

print(f'Somewhere in {destination}')
print(f'{type} - {total:.2f}')


