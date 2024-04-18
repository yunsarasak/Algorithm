

n = int(input())

meeting_list = list()

for i in range(n):
    begin, end = list(map(int, input().split()))

    meeting_list.append([begin, end])


# for item in meeting_list:
#     print(item)

#sorted(meeting_list, key=lambda x: (meeting_list[1], -meeting_list[0]))
meeting_list.sort(key=lambda x:(x[1], x[0]))


# for item in meeting_list:
#     print(item)

answer = 0

#젤 먼저 끝나는 회의의 시작 시간
begin_time = meeting_list[0][0]
#젤 먼저 끝나는 회의의 끝나는 시간
end_time = meeting_list[0][1]
current_index = 0
answer += 1

answer_list = list()
answer_list.append(0)

while begin_time <= meeting_list[current_index][1]:
    current_index += 1
    if current_index == n:
        break
    if end_time <= meeting_list[current_index][0]:
        answer+=1
        answer_list.append(current_index)
        begin_time = meeting_list[current_index][0]
        end_time = meeting_list[current_index][1]
    
print(answer)

# for i in answer_list:
#     print(meeting_list[i])