count_honey_for_winter = float(input())

done = False

line = input()
saving_honey = 0

while line != "Winter has come":
    bee_name = line
    honey_per_six_month = 0
    for month in range(1, 6 + 1):
        honey_per_month = float(input())
        honey_per_six_month += honey_per_month
        saving_honey += honey_per_month

        if month == 6 :
            if honey_per_six_month < 0:
                print(f"{bee_name} was banished for gluttony")

    if saving_honey >= count_honey_for_winter:
        print(f"Well done! Honey surplus {saving_honey - count_honey_for_winter:.2f}.")
        break
    line = input()


if count_honey_for_winter > saving_honey:
    print(f"Hard Winter! Honey needed {count_honey_for_winter - saving_honey:.2f}.")