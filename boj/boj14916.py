
N = int(input())

coin_count = 0


while N:
    #print(N)
    if N == 8:
        N -= 8
        coin_count +=4
    elif N ==6 :
        N -= 6
        coin_count += 3
    elif N==4:
        N -= 4
        coin_count += 2
    elif N == 2:
        N -= 2
        coin_count += 1
    elif N >= 5:
        N -= 5
        coin_count+=1
    else:
        N = 0
        coin_count = -1

print(coin_count)
