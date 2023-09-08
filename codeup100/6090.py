a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

result = a

for i in range(0, n - 1):
    result = result * m + d

print(result)
