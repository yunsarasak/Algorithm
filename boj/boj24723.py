#1
#1 1
#1 2 1
#1 3 3 1
#1 4 6 4 1
#1 5 10 10 5 1
#
#1 2 4 8 16 32

level = int(input())

answer = 1

for i in range(level):
    answer = answer * 2

print(answer)