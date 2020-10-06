from math import floor

income_in_lv = float(input())
average_success =float(input())
minimal_salary = float(input())

scholarship = floor(minimal_salary * 0.35)
scholarship2 = floor(average_success * 25)

if income_in_lv > minimal_salary :
    print("1You cannot get a scholarship!")

elif income_in_lv < minimal_salary:
    if average_success >= 4.50 :
        scholarship = floor(minimal_salary * 0.35)
    if average_success >= 5.50 :
        scholarship2 = floor(average_success * 25)
    elif scholarship > scholarship2:
        print(f"2You get a Social scholarship {scholarship} BGN")
    elif scholarship2 > scholarship:
        print(f"3You get a scholarship for excellent results {scholarship2} BGN")


elif income_in_lv < minimal_salary:
    if average_success >= 4.50:
        if average_success < 5.50 :
            print(f"4You get a Social scholarship {scholarship} BGN")
if average_success >= 5.50 :
    print(f"5You get a scholarship for excellent results {scholarship2} BGN")