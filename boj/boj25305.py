N, k = list(map(int, input().split()))

num_list = list(map(int, input().split()))

answer = sorted(num_list, reverse=True)

print(answer[k-1])