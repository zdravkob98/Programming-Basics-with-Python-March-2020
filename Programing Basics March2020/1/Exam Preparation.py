income = float(input())
count_mouth = int(input())
costs = float(input())

another_costs = income * 0.3

saving = income - costs - another_costs

total_saving = count_mouth * saving
print(f"She can save {(saving / income) * 100:.2f}%")
print(f"{total_saving:.2f}")
