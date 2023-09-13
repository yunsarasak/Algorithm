def factorial(_n:int):
    if _n <= 1:
        return 1
    else:
        return factorial(_n - 1) * _n


N = int(input())

print(factorial(N))