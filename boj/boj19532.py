a, b, c, d, e, f = list(map(int, input().split()))

#p for prime
ap = a
bp = b
cp = c
dp = d
ep = e
fp = f

#mult fomula1 by d
#mult fomula2 by a
ap = ap * d
bp = bp * d
cp = cp * d
dp = dp * a
ep = ep * a
fp = fp * a

#sub fomula2 - fomula1
ep = ep - bp
fp = fp - cp
y = fp / ep
x = (f - e * y)/d

print(int(x), int(y))
