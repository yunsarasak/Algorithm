dp = [ [ [ -1 for i in range(21) ] for i in range(21)] for i in range(21) ]

def rec(a, b, c):
    global dp

    if a > 20 or b> 20 or c>20:
        return rec(20, 20, 20)

    if dp[a][b][c] != -1:
        return dp[a][b][c]

    if a<=0 or b<=0 or c<=0:
        return 1
    elif a < b and b < c:
        dp[a][b][c] = rec(a, b, c-1) + rec(a, b-1, c-1) - rec(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = rec(a-1, b, c) + rec(a-1, b-1, c) + rec(a-1, b, c-1) - rec(a-1, b-1, c-1)
        return dp[a][b][c]

#print(dp[0][0][0])
#seq = 0

while True:
    num0, num1, num2 = list(map(int, input().split()))

    #exit
    if num0 == -1 and num1 == -1 and num2 == -1:
        break

    answer = rec(num0, num1, num2)
    #answer_line = f'w({0}, {1}, {2}) = {3}'
    #answer_line.format(num0, num1, num2, answer)

    #print(answer_line)
    print(f'w({num0}, {num1}, {num2}) = {answer}')


#for i in range(999):
#    my_str = '{0:03d}'.format(seq)
#    num0 = int(my_str[0])
#    num1 = int(my_str[1])
#    num2 = int(my_str[2])
#    print(num0, num1, num2)
#    print(rec(num0, num1, num2))
#    seq+=1

#my_str.format(number=seq)

#print(my_str[0])

#print(rec(0, 0, 0))