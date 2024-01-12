import sys

N = int(sys.stdin.readline())

imoji_count = 0
#imoji_send_list = dict()
visitors = set()

for i in range(N):
    input_string = sys.stdin.readline()

    if input_string == "ENTER\n":
        visitors.clear()
    else:
        if input_string not in visitors:
            imoji_count += 1
            visitors.add(input_string)

print(imoji_count)

    
