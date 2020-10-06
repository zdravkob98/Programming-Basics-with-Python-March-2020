from math import floor

income_in_lv = float(input())
average_success =float(input())
minimal_salary = float(input())

scholarship = floor(minimal_salary * 0.35)
scholarship2 = floor(average_success * 25)



if income_in_lv < minimal_salary:
    if average_success >= 4.50 :
        scholarship = floor(minimal_salary * 0.35)
        if  average_success >= 5.50 :
            scholarship2 = floor(average_success * 25)
            if scholarship > scholarship2:
                print(f"You get a Social scholarship {scholarship} BGN")
            if scholarship2 > scholarship:
                print(f"You get a scholarship for excellent results {scholarship2} BGN")
elif income_in_lv < minimal_salary:
    if average_success >= 4.50:
        if average_success < 5.50 :
            print(f"You get a Social scholarship {scholarship} BGN")
elif average_success >= 5.50 :
    print(f"You get a scholarship for excellent results {scholarship2} BGN")
elif minimal_salary > income_in_lv:
    if average_success > 4.50:
        print("You cannot get a scholarship!")


