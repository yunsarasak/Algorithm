N = input()

sum_of_each_digit = 0
digit_list = list(N)
is_there_zero = False
# 3의 배수인지 확인한다.
for digit in digit_list:
    sum_of_each_digit += int(digit)
    if digit == '0':
        is_there_zero = True
    #print("adding",digit)

if (sum_of_each_digit % 3) != 0 or (not is_there_zero):
    answer = -1
else:
    digit_list.sort(reverse=True)
    answer = "".join(digit_list)

print(answer)
        
