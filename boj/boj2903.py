n  = int(input())

def pow(_base:int, _exp:int):
    ret = 1
    for i in range(_exp):
        ret = ret * _base

    return ret


rect_in_row = pow(2, n)
#print("rect in row : ", rect_in_row)

point_in_row = rect_in_row + 1
#print("point in row : ", point_in_row)

num_of_point = point_in_row * point_in_row

print(num_of_point)