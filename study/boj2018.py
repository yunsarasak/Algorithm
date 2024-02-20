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

# 풀이2. 
# 홀수면 나눠떨어질 때 좌우로 +1 -1 해서 순열을 만들 수 있음
# ex) N == 15, 15//3 = 5        555          456
#                           5 -1, 5, 5+1  이런식
# 짝수면 .5 가 남아야 ㅜ먼가...

N = int(input())

answer = 0

#이어지는 수의 첫번째 수, 즉 시작 숫자를 저장하기 위한 변수
starting_number = 1

#이어지는 수의 인덱스
number_added = 0

while starting_number != N:
    sum = 0
    number_added = 0

    # 합이 입력을 넘어서면 리턴
    while sum < N:
        # 이어지는 수들을 차례로 더한다.
        sum+= starting_number+number_added

        # 합이 입력과 같다면, 조건을 만족하므로 가지수 +1
        if sum == N:
            answer += 1
            #print("%d to %d"%(starting_number, starting_number+number_added))
            break

        # 아니라면 다음 수까지 더해본다
        number_added += 1
    
    # 시작 하는 수를 1증가
    starting_number+=1

# N 하나만으로도 수열이므로 가지수 +1
answer += 1

print(answer)