import sys

num_of_stones = int(input())

dp = [0 for _ in range(num_of_stones)]

stepping_stones = list(map(int, input().split()))


# def GetDifference(_a:int, _b:int):
#     if _a > _b:
#         return _a - _b
#     else:
#         return _b - _a


# def GetForceNeeded(_from:int, _to:int):
#     global stepping_stones

#     _from -= 1
#     _to -= 1
    
#     #print("(%d - %d) * (1+|%d - %d|)"%(_to, _from, stepping_stones[_from], stepping_stones[_to]))
#     return (_to - _from) * (1 + GetDifference(stepping_stones[_from], stepping_stones[_to]))

dp[0] = 0
dp[1] = 1+abs(stepping_stones[0] - stepping_stones[1])

for i in range(2, num_of_stones):
    min_max_force_to_reach_to_i = sys.maxsize
    for j in range(i):
        force_needed = (i-j) * (1 + abs(stepping_stones[j] - stepping_stones[i]) )

        max_force_to_reach_to_i = max(force_needed, dp[j])

        if max_force_to_reach_to_i < min_max_force_to_reach_to_i:
            min_max_force_to_reach_to_i = max_force_to_reach_to_i

    dp[i] = min_max_force_to_reach_to_i

# print(dp[num_of_stones-1])


print(dp[num_of_stones-1])