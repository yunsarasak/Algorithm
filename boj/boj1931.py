#미팅룸 예약, greedy

#미팅일정중 가장 빨리 끝나는 회의만 그리디하게 선택하면 된다.
#따라서 회의가 끝나는 시간으로 스케쥴을 정렬하고
#끝나는 시간보다 같거나 이후시간대의 회의일 경우 정답 리스트에 추가한다.

N = int(input())

meetingSchedules = list()

for i in range(N):
    startTime, endTime = list(map(int, input().split()))

    meetingSchedule = [startTime, endTime]

    meetingSchedules.append(meetingSchedule)


#print(meetingSchedules)

#스케쥴을 끝나는 시간이 이른 순서대로 정렬
meetingSchedules.sort(key= lambda x:(x[1], x[0]))
#print(meetingSchedules)

#미팅 선택 함수
def GetNextMeeting( _meetingList:list, _startingTime:int, _skipCount:int ):
    ret = -1

    for i in range( _skipCount ,len(_meetingList)):
        if _startingTime <= _meetingList[i][0]:
            ret = i
            break
        elif i == len(_meetingList) - 1:
            ret = -1
    
    return ret

answer = 0
    
nextStartingTime = 0
skipCount = 0

while True:
    meetingIndex = GetNextMeeting( meetingSchedules, nextStartingTime, skipCount )
    if( meetingIndex == -1):
        break
    else:
        answer+=1

    skipCount = meetingIndex+1
    #print("selected index :", meetingIndex)
    nextStartingTime = meetingSchedules[meetingIndex][1]


print(answer)