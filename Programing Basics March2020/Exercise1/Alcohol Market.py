price_whiskey = float(input())
beer_in_liters = float(input())
wine_in_liters = float(input())
rakiya_in_liters = float(input())
whiskey_in_liters = float(input())


price_rakiya_in_liters = price_whiskey / 2
price_wine_in_liters = price_rakiya_in_liters - ((price_rakiya_in_liters / 100) * 40 )
price_beer_in_liters = price_rakiya_in_liters - (0.8 * price_rakiya_in_liters)

total_price_rakiya = price_rakiya_in_liters * rakiya_in_liters
total_price_wine = price_wine_in_liters * wine_in_liters
total_price_beer = price_beer_in_liters * beer_in_liters
total_price_whiskey = price_whiskey * whiskey_in_liters

total_price_all = total_price_rakiya + total_price_wine + total_price_beer + total_price_whiskey

print(f'{total_price_all:.2f}')