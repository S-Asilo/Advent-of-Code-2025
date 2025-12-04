f = open("InputDay3.txt", "r")

Password = 0
for line in f:
    # Throw away new line
    line = line[:-1]
    largest_number = 9
    while largest_number > 0:
        
        if line[:-1].find(str(largest_number)) != -1:
            break

        largest_number -= 1 
    
    ln_index = line.index(str(largest_number))
    line_substring = line[ln_index+1:]
    second_battery_list = []

    for battery in line_substring:
        second_battery_list.append(int(battery))
    
    second_battery_list.sort()
    # print(second_battery_list)
    # print(line)

    Password += (largest_number*10) + second_battery_list[-1]


print(Password)