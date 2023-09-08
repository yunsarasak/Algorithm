#input N, B
#N을 B진법으로

table = list()



remain = list()

for for_i in range( ord("9") - ord("0") + 1):
    table.append( ord("0") + for_i )

for for_i in range( ord("Z") - ord("A") + 1):
    table.append( ord("A") + for_i )

#print(table)

N, B = list(map(int, input().split()))
#print(N, B)

dividend = N
divisor = B

while dividend >= divisor:
    remain.append(dividend % divisor)
    dividend = dividend // divisor

remain.append(dividend)

for i in range(len(remain)):
    #print(len(remain)-1, "-", i)
    val = remain[len(remain)-1-i]
    print(chr(table[val]), end="")

