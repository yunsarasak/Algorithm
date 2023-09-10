fomula = input()

# Python3 code to demonstrate working of
# Splitting operators in String
# Using re.split()
import re
 
# initializing string
test_str = fomula
 
# printing original string
#print("The original string is : " + str(test_str))
 
# Using re.split()
# Splitting operators in String
res = re.split(r'(\D)', test_str)
 
# printing result
#print("The list after performing split functionality : " + str(res))

#print(res)

minusFlag = 0
sum = 0

for i in range(len(res)):
    if i % 2 == 0:
        # 숫자는 짝수번째. ( 0부터 시작하기에.)
        if(minusFlag == 1):
            sum -= int(res[i])
        else:
            sum += int(res[i])
    else:
        # 연산자는 홀수번째. ( 1부터.. )
        if res[i] == "-":
            if( minusFlag == 0):
                minusFlag = 1

print(sum)

