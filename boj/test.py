import subprocess
import sys
import os
from itertools import *

#print(len(sys.argv))

this_file_name = os.path.basename(__file__)

if len(sys.argv) != 3:
    print("Usage : [python", this_file_name, "mine others]")
    sys.exit()

my_file = sys.argv[1]
others_file = sys.argv[2]

#make inputs
#print("your command : [", "python", this_file_name, my_file, others_file, "]")

dataset = [i for i in range(1, 6)]

printList = list(permutations(dataset, 5))


for j in range(len(printList)):
    test_case = []
    test_case.append(5)
    test_case.extend(printList[j])
    #print(type(test_case))

    arg3 = ' '.join( str(e) for e in test_case)

    print(test_case)
    subprocess.run(["python", "comp.py", arg3])
    subprocess.run(["python", "boj12789.py", arg3])
    print("-------------")


#test_case = [5, 2, 1, 3, 4, 5]
#print(type(test_case))

#arg3 = ' '.join( str(e) for e in test_case)

#print(test_case)
#subprocess.run(["python", "comp.py", arg3])
#subprocess.run(["python", "boj12789.py", arg3])
#print("-------------")