#N, K = list(map(int, input().split()))

N = int(input())
next_offsets = list(map(int, input().split()))

origin = list()
for i in range(N):
    origin.append(i + 1)


answer = list()

cursor = 0
K = next_offsets[0]

while len(answer) != N-1:
    print(origin)
    print("cursor:", cursor)
    if cursor == -1:
        cursor = len(origin) - 1
    index = cursor
    #pop from origin
    next = origin.pop(index)
    print(next)


    #append to answer
    answer.append(next)

    K = next_offsets[next]

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