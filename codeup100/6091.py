d1, d2, d3 = input().split()

d1 = int(d1)
d2 = int(d2)
d3 = int(d3)

date = 1

while not ((date % d1 == 0) and (date % d2 == 0) and (date % d3 == 0)):
    date += 1

print(date)