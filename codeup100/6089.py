a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

poweredR = 1

for i in range(0, n - 1):
    poweredR = poweredR * r

result = a * poweredR


print(result)
