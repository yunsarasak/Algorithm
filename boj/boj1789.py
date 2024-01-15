S = int(input())

sum = 0
for i in range(1,S+1):
    sum += i

    if sum > S:
        i-=1
        break
   
print(i)