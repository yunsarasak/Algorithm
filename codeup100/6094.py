n = int(input())

lists = input().split()

for i in range(0, n):
    lists[i] = int(lists[i])

min = lists[0]

for i in range(0, n):
    if (lists[i] < min):
        min = lists[i]

print(min)