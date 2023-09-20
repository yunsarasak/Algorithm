N, K = list(map(int, input().split()))

origin = list()
isExist = list()
for i in range(N):
    origin.append(i + 1)
    isExist.append(1)

answer = list()

cursor = K % N - 1

while len(answer) != N-1:
    #print(origin)
    #print("cursor:", cursor)
    if cursor == -1:
        cursor = len(origin) - 1
    index = cursor
    #pop from origin
    next = origin.pop(index)
    #print(next)


    #append to answer
    answer.append(next)

    #get next index
    cursor = ((cursor + K) % (len(origin))) - 1

answer.append(origin.pop())


#print(answer)

print("<", sep="", end="")
for i in answer:
    print(i, sep="", end="")
    if i != answer[len(answer)-1]:
        print(", ", sep="", end="")

print(">")