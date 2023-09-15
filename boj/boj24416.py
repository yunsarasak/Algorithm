def fib(_n:int):
    if _n == 1 or _n ==2:
        fib.counter += 1
        return 1
    else:
        return ( fib(_n - 1) + fib(_n - 2))

def fibonacci(_n:int):
    f = list()
    f.append(0)
    f.append(1)
    f.append(1)

    for i in range(3, _n + 1):
        f.append(f[i -1] + f[i-2])
        fibonacci.counter += 1
    return f[_n]



N = int(input())

fib.counter = 0
fibonacci.counter = 0

fib(N)
fibonacci(N)

print(fib.counter, fibonacci.counter)

