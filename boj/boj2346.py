import sys

#N, K = list(map(int, sys.stdin.readline().split()))

N = int(sys.stdin.readline())
offsets = list(map(int, sys.stdin.readline().split()))

class Balloon:
    def __init__(self, _index, _offset):
        self.index = _index
        self.offset = _offset

    def print(self):
        print("[", self.index, ",", self.offset, "]")

def move_left():
    global cursor
    global balloon_list
    if cursor != 0:
        cursor = cursor - 1
    else:
        cursor = len(balloon_list) - 1

def move_right():
    global cursor
    global balloon_list
    if cursor != (len(balloon_list) - 1):
        cursor += 1
    else:
        cursor = 0
    
    if cursor > len(balloon_list):
        cursor = cursor % len(balloon_list)

balloon_list = list()

for i in range(N):
    balloon_list.append(Balloon(i+1, offsets[i]))


answer = list()

cursor = 0

count = 0

while len(answer) != N-1:
    offset = balloon_list[cursor].offset
    index = balloon_list[cursor].index

    #balloon_list[cursor].print()
    balloon_list.pop(cursor)

    if( offset < 0):
        pass
    else:
        move_left()

    #append answer
    answer.append(index)

    #increase cursor
    while( offset != 0 ):
        if( offset < 0 ):
            move_left()
            offset+=1
        else:
            move_right()
            offset-=1

answer.append(balloon_list[0].index)

for i in range(len(answer)):
    print(answer[i], end=" ")