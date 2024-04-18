import math

x, y, d, t = list(map(int, input().split()))


distance = math.sqrt(x*x + y*y)

distance_remain = distance
time_to_spend = 0

#print(distance)

while distance_remain > 0 and distance_remain > d:
    distance_remain -= d
    time_to_spend += t
    print("jump! from %d to %d"%(distance_remain+d,distance_remain))

while distance_remain > 0:
    distance_remain -= 1
    time_to_spend += 1
    print("walk from %d to %d"%(distance_remain+1, distance_remain))

print(time_to_spend)
