max = input()

max = int(max)

for i in range(1, max+1):
    if i % 3 == 0:
        continue
    print(i, end=" ")