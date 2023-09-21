#1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
#2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
#3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
#4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
#5: 덱에 들어있는 정수의 개수를 출력한다.
#6: 덱이 비어있으면 1, 아니면 0을 출력한다.
#7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
#8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.

#1 : pushleft
#2 : push
#3 : popleft
#4 : pop
#5 : len
#6 : is empty
#7 : peek left
#8 : peek

from collections import deque
import sys

def isEmpty(_deq:deque):
    if len(_deq) == 0:
        return 1
    else:
        return 0

def popleft(_deq:deque):
    if isEmpty(_deq):
        return -1
    else:
        return _deq.popleft()
    
def pop(_deq:deque):
    if isEmpty(_deq):
        return -1
    else:
        return _deq.pop()

def peekleft(_deq:deque):
    if isEmpty(_deq):
        return -1
    else:
        return _deq[0]

def peek(_deq:deque):
    if isEmpty(_deq):
        return -1
    else:
        return _deq[-1]

output = str()

my_deq = deque()

N = int(sys.stdin.readline())

for i in range(N):
    line = sys.stdin.readline().split()

    if line[0] == "1":
        my_deq.appendleft(int(line[1]))
    elif line[0] == "2":
        my_deq.append(int(line[1]))
    elif line[0] == "3":
        print(popleft(my_deq))
    elif line[0] == "4":
        print(pop(my_deq))
    elif line[0] == "5":
        print(len(my_deq))
    elif line[0] == "6":
        print(isEmpty(my_deq))
    elif line[0] == "7":
        print(peekleft(my_deq))
    elif line[0] == "8":
        print(peek(my_deq))
    else:
        break

    #print(my_deq)

#print("ansewer")
#print(output)
