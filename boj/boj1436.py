#666 이 들어간 수중에 작은 순서대로 N번째 수를 출력하는 문제

N = int(input())

count = 666

have666 = list()

while len(have666) != N:
    strCount = str(count)
    if strCount.find('666') != -1:
        have666.append(count)
    count+=1

print(have666[N-1])