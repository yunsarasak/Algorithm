N, K = list(map(int, input().split()))

cursor = 1
count = 0
answer = 0

while cursor <= N:
    #count 가 K보다 크다면 실패
    if count > K:
        answer = 0
        break

    #나눠지면 count ++
    if N % cursor == 0:
        count+=1

    #count == K 면 성공, 결과를 출력
    if count == K:
        answer = cursor
        break

    #아니면 계속 진행
    cursor+=1

print(answer)
