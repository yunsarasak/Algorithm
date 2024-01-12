


N = int(input())

num_list = list(map(int, input().split()))


#print("numlist", num_list)

num_min = min(num_list)
num_max = max(num_list)

print(num_min * num_max)