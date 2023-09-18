# 나의 코드
import sys

#n = int(input())
#print(len(sys.argv))
args = sys.argv[1]
arg_list = args.split(' ')

n = int(arg_list[0])
#print(n)
#standing = list(map(int, input().split()))

standing = list()
for i in range(n):
    standing.append(int(arg_list[1 + i]))

stack = []
target = 1
 
while standing:
    if standing[0] == target:
        standing.pop(0)
        target += 1
    else:
        stack.append(standing.pop(0))
 
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break
 
if not stack: 
    print('answer : Nice')
else:
    print('answer : Sad')
 
# 혹은 이렇게 작성해도 된다.
#print('Nice' if not stack else 'No')