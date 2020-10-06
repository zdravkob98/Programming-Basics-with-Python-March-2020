num =float(input())
metric = str(input())
output_metric =str(input())

if metric == 'mm':
    num = num / 1000
elif metric == 'cm' :
    num = num /100

if output_metric == 'mm':
    num = num * 1000
elif output_metric == 'cm':
    num = num * 100



print(f'{num:.3f}')