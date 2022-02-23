col, row = map(int,input().split())
rotate = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

matrix = []
for i in range(row):
    matrix.append(list(input()))

answer = matrix.copy()

#노드 순회
for i in range(0, col):
    for j in range(0, row):
        #지뢰인지 확인, 지뢰면 answer의 노드에 *할당
        if matrix[i][j] == "*":
                answer[i][j] = "*"
                continue
        #카운트 초기화
        subtotal = 0
        #8방 순회
        for x,y in rotate:
            #범위 확인
            if i + x < 0 or i + x > col-1 or j + y < 0 or j + y > row-1:
                continue
            #지뢰 확인되면 카운트 증가
            if matrix[i + x][j + y] == "*":
                subtotal = subtotal + 1
        #answer의 노드에 카운트 할당
        answer[i][j] = subtotal
        
for i in range(0, col):
    for j in range(0, row):
        print(answer[i][j], end="")
    print()