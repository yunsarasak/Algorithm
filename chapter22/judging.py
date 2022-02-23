input1, input2 = map(int, input().split()) 

a = [pow(2, i) for i in range(input1, input2 + 1)]
b = [a[i] for i in range(0, len(a)) if i != 1 and i != len(a)-2]

print(b)