from collections import Counter
test_case = int(input())

while test_case:
    test_case-=1

    num_applicant = int(input())
    applicant_line = list()
    applicant_drop_array = [1 for _ in range(num_applicant)]

    for _ in range(num_applicant):
        document_score, interview_score = list(map(int, input().split()))
        applicant_line.append([document_score, interview_score])

    #print(applicant_line)

    sorted_line = sorted(applicant_line, key=lambda item:item[0])
    #print(sorted_line)

    for i in range(num_applicant-1,0, -1):
        for j in range(i-1, -1, -1):
            #print("i:", i)
            #print("j:", j)
            #print("comapre", sorted_line[i][1] ,">", sorted_line[j][1] )
            if sorted_line[i][1] > sorted_line[j][1]:
                #print("j[%d] kill i[%d]"%(j,i))
                applicant_drop_array[i] = 0
                break
    
    drop_count = Counter(applicant_drop_array)
    #print("drop_count:", drop_count)
    
    survivor_count = drop_count[1]
    

    #print("survivor:",survivor_count)
    #for i in range(num_applicant):
    #    if applicant_drop_array[i] == 0:
    #        print(sorted_line[i])
    print(survivor_count)