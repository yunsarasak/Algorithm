def solution(dots):
    answer = 0
    xmin = 257
    xmax = -257
    
    ymin = 257
    ymax = -257
    
    
    for i in range(len(dots)):
        if xmin > dots[i][0]:
            xmin = dots[i][0]
        if xmax < dots[i][0]:
            xmax = dots[i][0]
        if ymin > dots[i][1]:
            ymin = dots[i][1]
        if ymax < dots[i][1]:
            ymax = dots[i][1]

    #get width
    width = xmax - xmin
    #get hight
    hight = ymax - ymin
    
    answer = width * hight
    return answer
