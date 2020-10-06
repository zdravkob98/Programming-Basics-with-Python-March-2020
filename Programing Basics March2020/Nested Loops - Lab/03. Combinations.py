n = int(input())
counter = 0
for i in range(0, n + 1):
    for o in range(0, n + 1):
        for p in range(0, n + 1):
            if i + o + p == n:
                counter += 1
print(counter)