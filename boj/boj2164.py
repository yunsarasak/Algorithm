import sys
from collections import deque

def DropTop(_list:list):
    _list.pop(0)
    return

def SendToBottom(_list:list):
    _list.append(_list.pop(0))
    return

def Init(_max:int):
    ret = [i for i in range(1, _max+1)]
    return ret

N = int(sys.stdin.readline())

#deck = Init(N)
#deck = [i for i in range(1, N+1)]
deck = deque()
for i in range(1,N+1):
    deck.append(i)

while len(deck) != 1:
    #print(deck)
    #DropTop(deck)
    #SendToBottom(deck)
    #print(deck[0])
    deck.popleft()
    deck.append(deck.popleft())


#print("answer :", end="")
print(deck[0])

#1, 3, 5, 7 ... odd max
#2, 6, 10 ... even max

