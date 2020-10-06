count_people = int(input())

all_bakery = 0


waffles = 0
cookies = 0
cakes = 0


for people in range(1 , count_people +1):
    name = input()
    line = input()

    cookies_sum = 0
    cakes_sum = 0
    waffles_sum = 0

    while line != "Stop baking!":

        type_sweets = line
        count_ready_sweets = int(input())
        all_bakery += count_ready_sweets


        if type_sweets == "cookies":
            cookies_sum += count_ready_sweets
            cookies += count_ready_sweets

        elif type_sweets == "cakes":
            cakes_sum += count_ready_sweets
            cakes += count_ready_sweets

        elif type_sweets == "waffles":
            waffles_sum += count_ready_sweets
            waffles += count_ready_sweets

        line = input()


    print(f"{name} baked {cookies_sum} cookies, {cakes_sum} cakes and {waffles_sum} waffles.")
print(f"All bakery sold: {all_bakery}")
total = cookies * 1.50 + cakes * 7.80 + waffles * 2.30
print(f"Total sum for charity: {total:.2f} lv.")

