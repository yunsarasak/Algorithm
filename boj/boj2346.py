#N, K = list(map(int, input().split()))

N = int(input())
offsets = list(map(int, input().split()))

class Balloon:
    def __init__(self, _index, _offset):
        self.index = _index
        self.offset = _offset

    def print(self):
        print("[", self.index, ",", self.offset, "]")

balloon_list = list()

for i in range(N):
    balloon_list.append(Balloon(i+1, offsets[i]))


answer = list()

cursor = 0

while len(answer) != N-1:
    offset = balloon_list[cursor].offset
    index = balloon_list[cursor].index

    #balloon_list[cursor].print()
    balloon_list.pop(cursor)
    if cursor == 0:
        cursor = len(balloon_list)
    else:
        cursor -= 1

    #append answer
    answer.append(index)

    #increase cursor
    cursor = cursor + offset

    #modify to valid
    if (cursor > len(balloon_list)):
        cursor = cursor % len(balloon_list) - 1
    elif (cursor < 0):
        while( cursor < 0 ):
            cursor+=len(balloon_list)

answer.append(balloon_list[0].index)


#print(answer)

print("<", sep="", end="")
for i in answer:
    print(i, sep="", end="")
    if i != answer[len(answer)-1]:
        print(", ", sep="", end="")

print(">")