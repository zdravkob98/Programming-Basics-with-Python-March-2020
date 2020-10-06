period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1 ,period + 1):
    if i % 3 == 0:
        if treated_patients < untreated_patients:
            doctors += 1
    count_patient = int(input())
    if count_patient >= doctors:
        untreated_patients += count_patient - doctors
    else:
        untreated_patients += 0

    if count_patient >= doctors:
        treated_patients += doctors
    else:
        treated_patients += count_patient


print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')