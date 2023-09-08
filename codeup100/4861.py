#https://codeup.kr/problem.php?id=4861

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

#DEBUG
#print(totalPopulation)

for i in range(students):
    gender, grade = list(map(int, input().split()))
    # 1 for difference between index which is starting 0 and grade which is starting 1
    totalPopulation[grade - 1][gender] += 1

#DEBUG
#print(totalPopulation)

roomCount = 0

for i in range(6):
    roomCount += calcNeededRoomForNYearsOld(totalPopulation[i], maxRoomPopulation)

print(roomCount)