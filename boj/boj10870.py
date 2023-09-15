def fib(_num:int):
    if _num == 2 or _num == 1:
        return 1
    elif _num == 0:
        return 0
    else:
        return fib(_num-1) + fib(_num-2)

N = int(input())

print(fib(N))