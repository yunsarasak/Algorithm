#https://codeup.kr/problem.php?id=4846

#read input
numSchools = int(input())

numStudents = [0 for i in range(numSchools)]
numApples = [0 for i in range(numSchools)]
numRemainder = [0 for i in range(numSchools)]

for i in range(numSchools):
    numStudents[i] ,numApples[i] = list(map(int, input().split()))

    numRemainder[i] = numApples[i] % numStudents[i]


#DEBUG
#print()
#for i in range(numSchools):
#    print(numStudents[i], end=" ")
#    print(numApples[i])

#DEBUG
#for i in range(numSchools):
#    print(numRemainder[i], end = " ")

print(sum(numRemainder))

