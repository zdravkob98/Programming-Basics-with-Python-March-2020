from math import floor

record_in_sec = float(input())
dist_in_meters = float(input())
sec_per_meter = float(input())

total_sec = dist_in_meters * sec_per_meter

final_sec = (dist_in_meters // 15 * 12.5) + total_sec



if final_sec <= record_in_sec:
    print(f" Yes, he succeeded! The new world record is {final_sec:.2f} seconds.")
else:
    print(f"No, he failed! He was {final_sec - record_in_sec:.2f} seconds slower.")