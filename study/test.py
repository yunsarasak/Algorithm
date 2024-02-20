

peer_count = int(input())


nCount = 0

for i in range(peer_count):
    nCount+=1

    if nCount % 5 == 1:
        print("header -----------------")

    print("%d peer blah"%nCount)

    if nCount % 5 == 0:
        print("total count = %d/256"%nCount)

if nCount % 5 == 0:
    pass
else:
    print("total count = %d/256"%nCount)
    