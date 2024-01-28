
N = int(input())

drain_counts = 0

def IsDasomWinner():
    global N
    global number_of_votes

    for i in range(1,N):
        if number_of_votes[i] >= number_of_votes[0]:
            return False

    return True

def DrainVote():
    global N
    global number_of_votes
    global drain_counts

    max_votes = max(number_of_votes)
    
    for i in range(1, N):
        if max_votes == number_of_votes[i]:
            number_of_votes[i] -= 1
            number_of_votes[0] += 1
            drain_counts += 1
            break

number_of_votes = [0 for i in range(N)]

for candidate in range(N):
    number_of_votes[candidate] = int(input())


while not IsDasomWinner():
    DrainVote()

print(drain_counts)