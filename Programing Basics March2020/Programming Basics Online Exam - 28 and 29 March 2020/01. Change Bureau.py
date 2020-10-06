bitcoin = int(input())
iona = float(input())
commission = float(input())


lev_bitcoin = bitcoin * 1168
dollar_iona = iona * 0.15
dollar_lev = dollar_iona * 1.76

lev = lev_bitcoin + dollar_lev
euro_lev = lev / 1.95


komisiiona = (euro_lev / 100) * commission


print(f'{euro_lev - komisiiona:.2f}')


