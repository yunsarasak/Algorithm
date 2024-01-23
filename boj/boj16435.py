
fruit_count, initial_length = list(map(int, input().split()))

fruit_list = list(map(int, input().split()))

fruit_list.sort()

current_index = 0
current_length = initial_length


while fruit_list[current_index] <= current_length:
    current_length+=1
    current_index+=1
    if current_index == fruit_count:
        break

    


# print(fruit_list)

print(current_length)