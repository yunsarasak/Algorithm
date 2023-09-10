
num_list = list()

for i in range(5):
    num = int(input())

    num_list.append(num)

num_list.sort()

#print(num_list)

sum = 0
for i in num_list:
    sum += i

avg = sum/5

print(int(avg), num_list[2])
