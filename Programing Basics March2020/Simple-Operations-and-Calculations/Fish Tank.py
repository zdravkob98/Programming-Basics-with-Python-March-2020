length = int(input())
width = int(input())
height = int(input())
occupied_percentage = float(input())

total_volume_in_centimeters= length * width * height
total_volume_in_liters = total_volume_in_centimeters*0.001

total_free_volume = total_volume_in_liters * (100 - occupied_percentage) /100

print(f'{total_free_volume:.3f}')