stack = list()
top = -1

def pop():
    global top
    stack.pop(top)
    top -= 1

def push(_num:int):
    global top
    stack.append(_num)
    top += 1

N = int(input())

for i in range(N):
    curr = int(input())

    if curr == 0:
        pop()
    else:
        push(curr)

sum = 0
for j in range(top+1):
    #print("add", stack[j])
    sum += stack[j]

print(sum)

