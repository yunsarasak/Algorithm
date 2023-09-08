def GetListSum( _list:list ):
    ret = 0
    for i in range(len(_list)):
        ret += _list[i]

    return ret

while True:

    n = int(input())

    if(n == -1):
        break

    curr_divisor = 1

    divisor_list = list()

    while curr_divisor < n:
        if n % curr_divisor == 0:
            divisor_list.append(curr_divisor)

        curr_divisor += 1

    list_sum = GetListSum( divisor_list )

    if(list_sum == n):
        print(n, "=", sep=" ", end=" ")
        
        for i in range(len(divisor_list)):
            print(divisor_list[i], end="")

            if(i == len(divisor_list)-1):
                print()
            else:
                print(" + ", end="")
    else:
        print(n, "is NOT perfect.", sep=" ")