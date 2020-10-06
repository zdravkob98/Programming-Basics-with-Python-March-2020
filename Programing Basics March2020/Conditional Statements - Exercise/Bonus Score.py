number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
elif number <1000:
    bonus = number * 0.20
elif number >= 1000 :
    bonus = number * 0.10

bonus2 = 0

if number % 2 == 0 :
    bonus2 = 1
elif number % 10 == 5 :
    bonus2 = 2
else :
    bonus2=0

#print(bonus)
#print(bonus2)
bonus_points = bonus + bonus2
final_points = number + bonus + bonus2

print(bonus_points)
print(final_points)
