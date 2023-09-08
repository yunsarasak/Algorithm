# 0.25, 0.1, 0.05, 0.01 in dallor
# 250, 100, 50, 10 in cent

q_cent = 25
d_cent = 10
n_cent = 5
p_cent = 1

# input 1 ~ 500

#output quarter, dime, nickel, penny

#get quarter

testCase = int(input())

while testCase != 0:
    change = int(input())
    remain = change
    
    q = 0
    while remain >= q * q_cent:
        q = q + 1
    
    q -= 1

    remain = remain - q*q_cent

    d = 0
    while remain >= d * d_cent:
        d = d + 1
    
    d -= 1
    remain = remain - d*d_cent

    n = 0
    while remain >= n * n_cent:
        n = n + 1
    
    n -= 1
    remain = remain - n*n_cent

    p = 0
    while remain >= p * p_cent:
        p = p + 1
    
    p -= 1

    remain = remain - p*p_cent
    
    
    print(q, d, n, p)

    testCase -= 1