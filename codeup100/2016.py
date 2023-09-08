n = int(input())

stringNum = input()

for i in range(n):
    if (n - i) % 3 == 0 and i != 0:
        print(",", end="")
    print(stringNum[i], end="")