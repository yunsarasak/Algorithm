
n = int(input())

cur = 1

while True:
    if(cur * cur > n):
        break
    else:
        cur += 1

print(cur - 1)