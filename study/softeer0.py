#https://softeer.ai/app/assessment/index.html?xid=102828&xsrfToken=3sE7xB2SJbyB2UUToj1KV60KMk0tIly0&testType=practice

import sys

# def MyPrint(message, *args):
#     #print(message % args)
#     return 0

def dfs(_path:list, _row, _col, _depth, _person_index):
    global n, m, answer
    #if out of index, return
    if _row < 0 or _row >= n:
        # MyPrint("out of index")
        return
    if _col < 0 or _col >= n:
        # MyPrint("out of index")
        return
    
    #if visited position, return
    for item in _path:
        if item[0] == _row and item[1] == _col:
            # MyPrint("redundant")
            return

    # append route
    _path.append([_row,_col])

    #if reaches max depth, check answer and return
    if _depth == 3:
        # MyPrint("append", _path)
        answer[_person_index].append(_path.copy())
        _path.pop()
        return

    #else go deeper
    _depth += 1

    #go left
    # MyPrint("from (%d, %d) to (%d, %d)"%(_row, _col, _row, _col-1))
    dfs(_path, _row, _col-1, _depth, _person_index)
    #go right
    # MyPrint("from (%d, %d) to (%d, %d)"%(_row, _col, _row, _col+1))
    dfs(_path, _row, _col+1, _depth, _person_index)
    #go up
    # MyPrint("from (%d, %d) to (%d, %d)"%(_row, _col, _row-1, _col))
    dfs(_path, _row-1, _col, _depth, _person_index)
    #go down
    # MyPrint("from (%d, %d) to (%d, %d)"%(_row, _col, _row+1, _col))
    dfs(_path, _row+1, _col, _depth, _person_index)

    #if tried all posibility, go shallower
    _path.pop()
    return
        

n, m = list(map(int, input().split()))

answer = [list() for _ in range(m)]

fruit_matrix = list()

for i in range(n):
    fruit_input = list(map(int, input().split()))
    fruit_matrix.append(fruit_input)

for person_index in range(m):
    row_input, col_input = list(map(int, input().split()))

    #index starts from 1
    row_input -= 1
    col_input -= 1

    temp_path = list()
    dfs(temp_path, row_input, col_input, 0, person_index)

    temp_path.clear()


# for k in range(m):
#     MyPrint(answer[k])

# for route in answer:
#     for item in route:
#         MyPrint(item)
#     MyPrint()

def GetMaxFruit():
    global answer

    # for route in answer:
    #     for item in route:
    #         MyPrint(item)
    #     MyPrint("")


    max = 0

    if m == 1:
        for j in range(len(answer[1])):
            sum = GetFruitSum(answer[0][i], None, None)
            if sum > max:
                # MyPrint("answer is ",answer[0][i],"and", answer[1][j])
                max = sum
    elif m == 2:
        for i in range(len(answer[0])):
            for j in range(len(answer[1])):
                sum = GetFruitSum(answer[0][i],answer[1][j], None)
                if sum > max:
                    # MyPrint("answer is ",answer[0][i],"and", answer[1][j])
                    max = sum
    else:
        for i in range(len(answer[0])):
            for j in range(len(answer[1])):
                for k in range(len(answer[2])):
                    sum = GetFruitSum(answer[0][i],answer[1][j], answer[1][k])
                    if sum > max:
                        # MyPrint("answer is ",answer[0][i],"and", answer[1][j])
                        max = sum

    

    return max

def GetFruitSum(_route_a:list, _route_b:list, _route_c:list):
    global fruit_matrix
    sum = 0
    set_union = set()
    #https://rollingsnowball.tistory.com/entry/from-list-to-set-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%A5%BC-%ED%95%B4%EC%8B%9C%ED%98%95-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%83%80%EC%9E%85%EC%9D%B8-%EC%85%8B%EC%9C%BC%EB%A1%9C-%EB%B3%80%ED%99%98%ED%95%98%EA%B8%B0
    if _route_a is None:
        pass
    else:
        set_a = set(list(map(tuple,_route_a)))
        set_union = set_union | set_a

    if _route_b is None:
        pass
    else:
        set_b = set(list(map(tuple,_route_b)))
        set_union = set_union | set_b

    if _route_c is None:
        pass
    else:
        set_c = set(list(map(tuple,_route_c)))
        set_union = set_union | set_c

    for i in set_union:
        sum += fruit_matrix[i[0]][i[1]]
    
    return sum
    

print(GetMaxFruit())


    
    


# for j in range(m):
#     col_input, row_input = list(map(int, input().split()))
#     friends_array[j].print_pos()


#print(fruit_matrix)


#test case
# 4 2
# 20 26 185 80
# 100 20 25 80
# 20 20 88 99
# 15 32 44 50
# 1 2
# 2 3