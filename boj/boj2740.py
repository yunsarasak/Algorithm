import sys

N, M = list(map(int,(sys.stdin.readline().split())))
#print(N, M)
matrix_a = list()

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix_a.append(row)


# for i in range(N):
#     print(matrix_a[i])


M, K = list(map(int,(sys.stdin.readline().split())))
#print(M, K)
matrix_b = list()

for _ in range(M):
    row = list(map(int, sys.stdin.readline().split()))
    matrix_b.append(row)

# for i in range(M):
#     print(matrix_b[i])

#print()
matrix_multiplied = [[0 for _ in range(K)] for _ in range(N)]

#print(matrix_multiplied)

for ri in range(N):
    for ci in range(K):
        row = matrix_a[ri]
        for cii in range(M):
            matrix_multiplied[ri][ci] += row[cii] * matrix_b[cii][ci]

for ri in range(N):
    for ci in range(K):
        print(matrix_multiplied[ri][ci], end=" ")
    print()