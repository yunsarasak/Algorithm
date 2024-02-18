#https://www.acmicpc.net/problem/2018

# 1
# 2
# 3, 1+2
# 4
# 5, 2+3
# 6, 1+2+3
# 7, 3+4
# 8, 
# 9, 4+5
# 10, 1+2+3+4

N = int(input())

divisor = 1
answer = 0

def PrintAnswerList(_center, _length):
    if _length % 2 == 0:
        answer_list = []
        starting_number = int(_center - 0.5)
        for i in range(_length):
            answer_list.append(starting_number + i)
    else:
        answer_list = []
        starting_number = _center - (_length//2)
        for i in range(_length):
            answer_list.append(starting_number + i)

    print(answer_list)


while divisor <= N:
    if divisor % 2 == 0:
        #짝수면... .5가 나와야하나?
        # 18 % 4 = 2
        # 18 / 4 = 4.5
        # 4.5 4.5 4.5 4.5 -> 4.5 4 5 4.5
        # 3, 4, 5, 6

        # 14 % 4 = 2
        # 14 / 4 = 3.5
        # 3.5 3.5 3.5 3.5 -> 2 3 4 5

        # 10 % 4 = 2
        # 10 / 4 = 2.5
        # 2.5 2.5 2.5 2.5 -> 1 2 3 4

        # 33 % 6 = 3
        # 33 / 6 = 5.5
        # 5.5 5.5 5.5 5.5 5.5 5.5 -> 3 4 5 6 7 8

        # 15 % 2 = 1
        # 15 / 2 = 7.5
        # 7.5 7.5 -> 7 8

        if (N/divisor) - N//divisor == 0.5:
            print("%d / %d = %.1f"%(N, divisor, (N/divisor)))
            center = N / divisor
            # print(center)
            length = divisor
            if center - (length//2) < 0:
                answer-=1
            # else:
            #     PrintAnswerList(center, length)

            answer += 1
    else:
        #홀수면 연속으로 만들 수 있음
        #ex) 15 % 3 = 0,
        #15 // 3 = 5
        # 5 5 5 -> 4 5 6, 이렇게 왼,오 1씩 더하고 뺌
        if N % divisor == 0:
            center = N//divisor
            length = divisor
            if(length == N):
                divisor+=1
                continue
            # PrintAnswerList(center, length)
            answer += 1

    divisor += 1

print(answer)