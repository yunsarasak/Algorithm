from collections import Counter
import sys

N = int(sys.stdin.readline())

sum = 0

num_list = []

for _ in range(N):
    num_input = int(sys.stdin.readline())
    num_list.append(num_input)
    sum += num_input

num_list.sort()

#산술 평균
average = round( sum / N )

#중앙값
center = num_list[N//2]

#최빈값
counts = Counter(num_list)

common_number_list = counts.most_common()
sorted_common_list = sorted(common_number_list, key=lambda item : (item[1], -item[0]), reverse=True)
#print("common:", sorted_common_list)

list_max = len(sorted_common_list)

if len(sorted_common_list) == 1:
    most_common = sorted_common_list[0][0]
else:
    if sorted_common_list[0][1] == sorted_common_list[1][1]:
        most_common = sorted_common_list[1][0]
    else:
        most_common = sorted_common_list[0][0]

#범위
from_to_range = num_list[N-1] - num_list[0]

print( average )
print( center )
print( most_common )
print( from_to_range )

