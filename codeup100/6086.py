input = input()

input = int(input)

cur = 1
sum = 0


while True:
    sum = sum + cur
    if sum >= input:
        break
    cur = cur + 1

print(sum)