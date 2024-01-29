
N, K = list(map(int, input().split()))

bottle_count = 0
water_added = 0

if N <= K:
    print(0)
else:
    while True:
        remain = N + water_added
        bottle_count = 0

        # merge as many as possible
        while (remain != 0):
            if remain % 2 == 1:
                bottle_count += 1
            remain = remain // 2

        # check success
        if bottle_count <= K:
            break
        #else continue with extra water

        water_added += 1

    print(water_added)

            
            
