


peer_count = int(input())


nCount = 0

print("header -----------------")

for i in range(peer_count):
    nCount+=1

    if (nCount >= 5) and (nCount-1) % 5 == 0:
        print("total count = %d/256"%(nCount))

        print("header -----------------")

    print("%d peer blah"%nCount)

print("total count = %d/256"%nCount)