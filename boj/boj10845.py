

my_queue = list()

size = int(input())

answer = list()

def MyPrint(_arg_to_print):
    global answer
    answer.append(_arg_to_print)

while size > 0:
    #print(size)
    command = input().split()
    #print(command)

    if command[0] == "push":
        #print("push~~~~~~~~~~~~~~~~~~~~~")
        my_queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(my_queue) == 0:
            MyPrint(-1)
        else:
            MyPrint(my_queue[0])
            my_queue.pop(0)
    elif command[0] == "size":
        MyPrint(len(my_queue))
    elif command[0] == "empty":
        if(len(my_queue)) == 0:
            MyPrint(1)
        else:
            MyPrint(0)
    elif command[0] == "front":
        if(len(my_queue)) == 0:
            MyPrint(-1)
        else:
            MyPrint(my_queue[0])
    elif command[0] == "back":
        if(len(my_queue)) == 0:
            MyPrint(-1)
        else:
            MyPrint(my_queue[-1])
    else:
        #print(command)
        continue

    size -=1

for word in answer:
    print(word)