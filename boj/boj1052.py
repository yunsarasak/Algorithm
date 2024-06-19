
N, K = list(map(int, input().split()))

def pow(_base, _exponent):
    answer = 1

    for i in range(_exponent):
        answer *= _base

    return answer

twos_squares = list()

element = 1

max_limit = pow(10, 7)

while( element < max_limit ):
    twos_squares.append(element)
    element = element * 2

print(twos_squares)

target_numbers = twos_squares.copy()

for item_index in range(len(target_numbers)):
    target_numbers[item_index] *= K

print(target_numbers)

#if N exceed target number, that's the target
for item_index in range(len(target_numbers)):
    print("compare:", N, ", ", target_numbers[item_index] )
    if N <= target_numbers[item_index]:
        break

answer = target_numbers[item_index] - N

print(answer)


