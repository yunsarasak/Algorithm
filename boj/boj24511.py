#if stack, LIFO. so skip operate
#else queue, we care data in it
from collections import deque
import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

Bp = list(map(int, sys.stdin.readline().split()))


#queue_count = 0
#
#for i in range(len(A)):
#    if A[i] == 0:
#        queue_count+=1
#    else:
#        pass

#print(queue_count)

#delete stakcs from list
#cursor = 0
#while cursor != len(B):
#    if A[cursor] == 1:
#        A.pop(cursor)
#        Bp.pop(cursor)
#        cursor -=1
#
#    cursor+=1

B = deque()
for i in range(len(A)):
    if(A[i] == 0):
        B.append(Bp[i])

#print("list without stakcs:", end=" ")
#print(B)

#B_list = deque()
#
#for i in range(len(B)):
#    B_list.append(list())
#    B_list[i].append(B[i])
#
#def FuncOnce(_new_num:int):
#    global B_list
#    num_poped = _new_num
#
#    for i in range(len(B)):
#        B_list[i].append(num_poped)
#        num_poped = B_list[i].pop(0)
#
#    return num_poped

M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

for j in range(M):
    B.appendleft(C[j])

answer = list()

for i in range(M):
    print(B.pop(), end=" ")

print()


#at first, I under stand this problem straight up. so write code straight up.
#problem solved but timed out. then I found entire B list runs like queue.
#so remove previously defined function FuncOnce then use deque. problem solved.