
def PrintMatrix(_mat:list[list[int]]):
    for row in _mat:
        for element in row:
            print(element, end=' ')
        print()

    return


def FindLongestPath(_mat:list[list[int]], starting_pc:int):
    global num_of_pc
    return_path = list()

    return_path.push(starting_pc)

    current_pc = starting_pc
    
    #find longest path from starting pc
    #while( ... ):

    return
        
    
    

    

num_of_pc, num_of_dependancy, hacked_pc_id = list(map(int, input().split()))

#print( num_of_pc, num_of_dependancy, hacked_pc_id )


# to      [0] [1] [2] [3]
# from[0]  0   0   0   0
# from[1]  0   0   3   0
# from[2]  0   0   0   0
# from[3]  0   0   0   0

# matrix[1][2] : time spent for hacking pc 2, from 1. in this case 3 sec.


matrix = [[0 for i in range(num_of_pc)] for i in range(num_of_pc)]

#PrintMatrix(matrix)


for i in range(num_of_dependancy):
    to_be_hacked, already_hacked, time_to_hack = list(map(int, input().split()))
    #print(to_be_hacked, already_hacked, time_to_hack)

    #convert to index
    already_hacked -= 1
    to_be_hacked -= 1

    matrix[already_hacked][to_be_hacked] = time_to_hack

FindLongestPath(matrix, hacked_pc_id - 1)
    
    

#PrintMatrix(matrix)