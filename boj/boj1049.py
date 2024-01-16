num_string_needed, num_brand = list(map(int, input().split()))

min_cost_for_single = 1001
min_cost_for_package = 1001

for _ in range(num_brand):
    cost_for_package, cost_for_single = list(map(int, input().split()))

    #print("compare", cost_for_single, ",", min_cost_for_single)
    if cost_for_single < min_cost_for_single:
        min_cost_for_single = cost_for_single

    if cost_for_package < min_cost_for_package:
        min_cost_for_package = cost_for_package


# print(min_cost_for_single)
# print(min_cost_for_package)

total_cost = 0

# print("single:", min_cost_for_single)
# print("pack:", min_cost_for_package)
if min_cost_for_single*6 < min_cost_for_package:
    total_cost = min_cost_for_single * num_string_needed
    num_string_needed = 0

while num_string_needed>0:
    #print(num_string_needed)
    if num_string_needed < 6:
        if num_string_needed * min_cost_for_single < min_cost_for_package:
            total_cost += min_cost_for_single * num_string_needed
            num_string_needed -= num_string_needed
        else:
            total_cost += min_cost_for_package
            num_string_needed -= 6
    else:
        total_cost += min_cost_for_package
        num_string_needed -= 6

print(total_cost)