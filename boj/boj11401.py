N, K = list(map(int,input().split()))

def combi(n:int, m:int):
    if (m == 0) or (m == n):
        return 1
    else:
        return combi(n-1, m-1) + combi(n-1, m)

answer = combi(N, K)

answer = answer % 1000000007

print(answer)