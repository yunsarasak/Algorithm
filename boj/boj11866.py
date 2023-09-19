N, K = list(map(int, input().split()))

origin = list()
isExist = list()
for i in range(N):
    origin.append(i + 1)
    isExist.append(1)

#print(origin)

answer = list()

cursor = 0

while len(answer) != N:
    # count 1 by 1, 
    cursor = (cursor + K) % (len(origin) - len(answer))
    
    # pop elm on origin
    origin.pop(cursor)
    
    # append into answer

    target_index = K % list_len - 1
    poped_num = origin.pop(target_index)
    answer.append(poped_num)
    list_len = len(origin) + 1

print(answer)