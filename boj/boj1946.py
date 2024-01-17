import sys
test_case = int(sys.stdin.readline().rstrip())

while test_case:
    test_case-=1

    num_applicant = int(sys.stdin.readline().rstrip())
    applicant_line = list()

    for _ in range(num_applicant):
        document_score, interview_score = list(map(int, sys.stdin.readline().rstrip().split()))
        applicant_line.append([document_score, interview_score])

    #print(applicant_line)

    sorted_line = sorted(applicant_line, key=lambda item:item[0])
    #print(sorted_line)

    # the first man always win in first match, so should be chosen.
    num_of_chosen = 1
    choice_threshold = sorted_line[0][1]
    for i in range(1,num_applicant):
        # then compare second score, if defeat in second match, he or she will be chosen
        if choice_threshold > sorted_line[i][1]:
            # the next threshold should be updated to current applicant
            # so, next applicant defeat this applicant then be chosen because
            # altough lose the first match, but win in second match. ( because they are sorted in ascending order )
            choice_threshold = sorted_line[i][1]
            num_of_chosen += 1

    print(num_of_chosen)