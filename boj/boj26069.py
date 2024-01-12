import sys

meet_count = int(sys.stdin.readline())

dancing_people = set()

dancing_people.add("ChongChong")

for _ in range(meet_count):
    person_a, person_b  = sys.stdin.readline().split()
    #print(person_a, person_b)

    if (person_a in dancing_people) or (person_b in dancing_people):
        dancing_people.add(person_a)
        dancing_people.add(person_b)

print(len(dancing_people))
