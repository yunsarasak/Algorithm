def IsAcceptable(input):
    if input % 3 == 0:
        return False
    
    input_string = str(input)
    
    if "3" in input_string:
        #print(input_string+" has 3")
        return False
    #if "6" in input_string:
    #    print(input_string+" has 6")
    #    return False
    #if "9" in input_string:
    #    #print(input_string+" has 9")
    #    return False
    
    #print(input_string+" is acceptable")
    return True


def solution(n):
    three_ex_num = 0
    actual_num = 0
    
    while n != actual_num:
        three_ex_num += 1
        
        while not IsAcceptable(three_ex_num):
            # acceptable하지 않다면 acceptable 할 때까지 three_ex_num + 1
            three_ex_num += 1
        actual_num += 1
    
    answer = three_ex_num
    return answer
