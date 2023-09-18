from collections import deque
import sys

top = -1
stack = deque()

def push(_num:int):
    global stack
    global top
    stack.append(_num)
    top+=1
    #print("push", _num)

def pop():
    global stack
    global top
    if( top == -1 ):
        ret = -1
    else:
        ret = stack.pop()
        top-=1

    return ret

def peek():
    global stack
    global top
    if( top == -1):
        return -1
    else:
        return stack[top]

args = sys.argv[1]
arg_list = args.split(' ')
#N = int(input())
N = int(arg_list[0])

count = 1
answer = "Nice"

#queue = list(map(int, input().split()))
queue = deque()
for i in range(N):
    queue.append(int(arg_list[1 + i]))


#print(queue)

for i in range(N):
    #print(i, "iter")
    num = queue[i] 

    if count == num:
        count+=1
        #print(num, "pass")
        continue
    elif count == peek():
        temp = pop()
        count+=1
        i -=1
        #print(temp, "poped")
        continue
    else:
        if (peek() == -1) or (peek() > num):
            push(num)
            #print(num, "pushed")
            continue
        else:
            answer = "Sad"
            break
        
print(answer)