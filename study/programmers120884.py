def solution(chicken):
    answer = -1
    # answer += 치킨 개수
    answer += chicken

    # 쿠폰 수 = 치킨 개수 // 10 ( 몫)
    num_coupon = chicken // 10

    # 만약, 쿠폰수가 10개 이상이다
    if num_coupon > 10:
        #   쿠폰수
        answer += num_coupon // 10
        new_coupon = num_coupon // 10
        
        num_coupon = num_coupon % 10
        num_coupon += new_coupon

    return answer