#https://codeup.kr/problem.php?id=4866
# editted from https://codeup.kr/problem.php?id=4861

#read inputs

def calcNeededRoom(_numStudents : int, _numMaxRoomPop : int):
    if _numStudents % _numMaxRoomPop != 0:
        return (_numStudents + _numMaxRoomPop) // _numMaxRoomPop
    else:
        return (_numStudents) // _numMaxRoomPop

def calcNeededRoomForNYearsOld(_classMates : list, _numMaxRoomPop : int):
    femalePop = calcNeededRoom(_classMates[0], _numMaxRoomPop)
    malePop = calcNeededRoom(_classMates[1], _numMaxRoomPop)
    return femalePop + malePop

students, maxRoomPopulation = list(map(int,input().split()))

#init table
#0 for female, 1 for male
classPopulation = [0, 0]
#DEBUG
#print(population)

#totalPopulation[ grade ][ gender ]
totalPopulation = [classPopulation.copy() for i in range(6)]

gradePair = [ [0, 0] for i in range(3)]

#DEBUG
#print(totalPopulation)

for i in range(students):
    gender, grade = list(map(int, input().split()))
    # 1 for difference between index which is starting 0 and grade which is starting 1
    totalPopulation[grade - 1][gender] += 1

    if grade == 1 or grade == 2:
        gradePair[0][gender] += 1
    elif grade == 3 or grade == 4:
        gradePair[1][gender] += 1
    else:
        gradePair[2][gender] += 1

roomCount = 0

#DEBUG
#for i in range(3):
#    print(gradePair[i])

#DEBUG
#print(totalPopulation)

#get 1,2 grade room count
student12 = gradePair[0][0] + gradePair[0][1]

if student12 % maxRoomPopulation == 0:
    roomCount += student12 // maxRoomPopulation
else:
    roomCount += (student12 // maxRoomPopulation) + 1

#get 3,4 grade room count
student34_female = gradePair[1][0]
student34_male = gradePair[1][1]

if student34_female % maxRoomPopulation == 0:
    roomCount += student34_female // maxRoomPopulation
else:
    roomCount += (student34_female // maxRoomPopulation) + 1

if student34_male % maxRoomPopulation == 0:
    roomCount += student34_male // maxRoomPopulation
else:
    roomCount += (student34_male // maxRoomPopulation) + 1

#get 5,6 grade room count
student56_female = gradePair[2][0]
student56_male = gradePair[2][1]

if student56_female % maxRoomPopulation == 0:
    roomCount += student56_female // maxRoomPopulation
else:
    roomCount += (student56_female // maxRoomPopulation) + 1

if student56_male % maxRoomPopulation == 0:
    roomCount += student56_male // maxRoomPopulation
else:
    roomCount += (student56_male // maxRoomPopulation) + 1

#for i in range(6):
#    roomCount += calcNeededRoomForNYearsOld(totalPopulation[i], maxRoomPopulation)

print(roomCount)