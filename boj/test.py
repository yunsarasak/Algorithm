import subprocess
import sys
import os

#print(len(sys.argv))

this_file_name = os.path.basename(__file__)

if len(sys.argv) != 3:
    print("Usage : [python", this_file_name, "mine others]")
    sys.exit()

my_file = sys.argv[1]
others_file = sys.argv[2]

#make inputs
#print("your command : [", "python", this_file_name, my_file, others_file, "]")


while True:
    test_case = [5, 5, 4, 1, 3, 2]
    #print(type(test_case))

    arg3 = ' '.join( str(e) for e in test_case)

    subprocess.run(["python", "comp.py", arg3])
    subprocess.run(["python", "boj12789.py", arg3])

