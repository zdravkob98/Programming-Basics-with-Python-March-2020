budget = int(input())
beach_towel = float(input())
percentage = int(input())


umbrella_price = (beach_towel / 3) * 2
flip_flops = umbrella_price * 0.75
beach_bag_price = (flip_flops + beach_towel) / 3

procent = ((beach_towel + umbrella_price + flip_flops + beach_bag_price) / 100 ) * percentage
total = (beach_towel + umbrella_price + flip_flops + beach_bag_price) - procent

if budget >= total:
    print(f"Annie's sum is {total:.2f} lv. She has {budget - total:.2f} lv. left.")
else:
    print(f"Annie's sum is {total:.2f} lv. She needs {total - budget:.2f} lv. more.")


