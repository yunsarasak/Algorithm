
A, B = input().split()

min_a = [0 for i in range(len(A))]
min_b = [0 for i in range(len(B))]
max_a = [0 for i in range(len(A))]
max_b = [0 for i in range(len(B))]

#get min
for i in range(len(A)):
    if A[i] == '5':
        max_a[i] = '6'
    else:
        max_a[i] = A[i]

for i in range(len(B)):
    if B[i] == '5':
        max_b[i] = '6'
    else:
        max_b[i] = B[i]

#get max
for i in range(len(A)):
    if A[i] == '6':
        min_a[i] = '5'
    else:
        min_a[i] = A[i]

for i in range(len(B)):
    if B[i] == '6':
        min_b[i] = '5'
    else:
        min_b[i] = B[i]

i_min_a = ''.join(min_a)
i_min_b = ''.join(min_b)

i_max_a = ''.join(max_a)
i_max_b = ''.join(max_b)


print(int(i_min_a)+int(i_min_b), int(i_max_a)+int(i_max_b))