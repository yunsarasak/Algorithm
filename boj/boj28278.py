import sys
top = -1

stack = list()

#1 : push
#2 : pop
#3 : count
#4 : isEmpty
#5 : peek

def MyPrint1(_str):
    print("[", end="")
    print(_str, end="")
    print("]")

def MyPrint(_str):
    print(_str)

lineCount = int(sys.stdin.readline())

for i in range(lineCount):
    inputString = sys.stdin.readline()

    if inputString[0] == "1":
        op, val = inputString.split()
        stack.append(int(val))
        top += 1
    elif inputString[0] == "2":
        if top != -1:
            out = stack.pop(top)
            MyPrint(out) 
            top -= 1
        else:
            MyPrint("-1")
    elif inputString[0] == "3":
        MyPrint(top + 1)
    elif inputString[0] == "4":
        if top == -1:
            MyPrint("1")
        else:
            MyPrint("0")
    else:
        if top == -1:
            MyPrint("-1")
        else:
            MyPrint(stack[top])