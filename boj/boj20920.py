import sys

num_words, length_threashold = list(map(int, sys.stdin.readline().split()))

#print( num_words, length_threashold )

#word sets
# [word]
#       [count]
word_sets = dict()


for _ in range(num_words):
    word_to_add = sys.stdin.readline().strip()
    if len(word_to_add) >= length_threashold:
        if word_to_add in word_sets:
            word_sets[word_to_add] += 1
        else:
            word_sets[word_to_add] = 1

#print("before arrangement")
#print(word_sets.items())


#print("after arrangement")
sorted_sets = sorted(word_sets.items(), key=lambda item : ( -item[1], -len(item[0]), item[0] ) )

for i in sorted_sets:
    print(i[0])
#print(sorted_sets)

