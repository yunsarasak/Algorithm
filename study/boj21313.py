N = int(input())

for i in range(N-1):
    if i%2 == 0:
        print("1 ", end="")
    else:
        print("2 ", end="")

if N %2 == 0:
    print("2")
else:
    print("3")