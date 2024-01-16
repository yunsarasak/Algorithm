
N = int(input())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

sum = 0

for _ in range(N):
    min_value = min(list_a)
    max_value = max(list_b)
    sum += min_value * max_value
    list_a.remove(min_value)
    list_b.remove(max_value)

print(sum)