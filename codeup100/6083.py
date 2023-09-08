r, g, b = input().split()

my_count = 0

r = int(r)
g = int(g)
b = int(b)


for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k, sep=" ")
            my_count = my_count + 1

print(my_count)