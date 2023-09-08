#input N, B

def pow( _base:int, _exp:int):
    ret = 1
    for i in range(_exp):
        ret = ret * _base
    
    return ret

table = list()

for for_i in range( ord("9") - ord("0") + 1):
    table.append( ord("0") + for_i )

for for_i in range( ord("Z") - ord("A") + 1):
    table.append( ord("A") + for_i )

#print(table)

N, B = input().split()

B = int(B)

ret = 0

#for i in range(len(N)):
#    print(N[i])

for i in range(len(N)):
    #from 1 to end

    # example, 12345, B is 10
        # when i is 0,
        # deci = 5, val = 10^0
        # when i is 1,
        # deci = 4, val = 10^1
    deci = table.index(ord(N[len(N) - i - 1]))
    val = pow(B, i)
    #print(deci, "*", val, "=", deci * val)
    ret += (val * deci)
    #print(pow(2, i))
    #val = 1

print(ret)