meters = float(input())
total_price = meters * 7.61
discount = total_price * 0.18
total_price_with_discount = total_price - discount

print(f'The final price is: {total_price_with_discount:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')
