
originString = input()

end = len(originString)

cursor = 0

answer = "YES"

while cursor != end:
    #2 pi, ka
    word2 = originString[cursor:cursor+2]
    if word2 == "pi" or word2 == "ka":
        cursor += 2
        #print(word2, "cursur now : ", cursor)
        continue
    
    #3 chu
    word3 = originString[cursor:cursor+3]
    if word3 == "chu":
        cursor += 3
        #print(word3, "cursur now : ", cursor)
        continue

    #else reach here, answer is no
    answer = "NO"
    break
    
print(answer)
