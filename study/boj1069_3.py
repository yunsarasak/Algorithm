import math

x, y, d, t = list(map(int, input().split()))


distance_to_go = math.sqrt(x*x + y*y)

answer = dict()
#walk only
answer['case1'] = distance_to_go

#jump only
if distance_to_go < d:
    answer['case2'] = 2 * t
else:
    count = 0
    remain_distance = distance_to_go
    while remain_distance > d:
        remain_distance -= d
        count += 1
    answer['case2'] = (count+1) * t

#jump and walk
remain_distance = distance_to_go
count = 0
while remain_distance > d:
    remain_distance -= d
    count += 1
    
answer['case3'] = count * t + remain_distance

answer['case4'] = (count+1)* t + (d - remain_distance)

candidate = list()

for key in answer:
    candidate.append(answer[key])

print(min(candidate))