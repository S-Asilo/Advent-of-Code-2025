f = open("InputDay3.txt", "r")

Password = 0
for line in f:
    # Throw away new line
    line = line[:-1]

    buffer = 0
    Maximum_allowed_index = -12
    while Maximum_allowed_index < 0:
        largest_number = 9
        while largest_number > 0:
            if Maximum_allowed_index == -1:
                if line.find(str(largest_number)) != -1:
                    break
            else:
                if line[:Maximum_allowed_index+1].find(str(largest_number)) != -1:
                    break

            largest_number -= 1 
        
        ln_index = line.index(str(largest_number))
        line = line[ln_index+1:]
        Maximum_allowed_index += 1
        Password += largest_number * ( 10 ** (Maximum_allowed_index * -1) )

print(Password)