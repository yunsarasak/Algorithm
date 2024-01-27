hight, width = list(map(int, input().split()))

if hight == 1:
    answer = 1
elif hight == 2:
    if width == 1 or width == 2:
        answer = 1
    elif width == 3 or width == 4:
        answer = 2
    elif width == 5 or width == 6:
        answer = 3
    else:
        answer = 4
else:
    # upup, downdown, up, down, [up | down]...
    # 1 , 1, 2, 2 => 6 + 1
    # 100000
    # 000000
    # 000000
    if width == 1:
        answer = 1
    elif width == 2:
        answer = 2
    elif width == 3:
        answer = 3
    elif width == 4:
        answer = 4
    elif width == 5:
        answer = 4
    elif width == 6:
        answer = 4
    elif width >= 7:
        # answer = 5 + alpha
        # moving up, down, upup, downdown equals 7
        alpha = width - 7
        answer = 5 + alpha
        
print(answer)
