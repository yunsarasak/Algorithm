max = input()

max = ord(max)

max = max - ord("A") + 10

for i in range(max, max+1):
    for j in range(1, 16):
        print('%X'%i, '*%X'%j, '=%X'%(i * j), sep="")