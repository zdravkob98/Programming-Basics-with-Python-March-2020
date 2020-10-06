n = int(input())
reached_n = False
po_kolko_chisla_na_red_da_printq = 1
current_number = 1

while not reached_n:
    for i in range(1, po_kolko_chisla_na_red_da_printq + 1):
        print(current_number, end=' ')
        current_number += 1
        if current_number > n:
            reached_n = True
            break
    po_kolko_chisla_na_red_da_printq += 1
    print()
7


