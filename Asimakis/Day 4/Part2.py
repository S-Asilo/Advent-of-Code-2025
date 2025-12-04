import math
f = open("InputDay4.txt", "r")


Warehouse = []
for line in f:
    row = []
    for entry in line[:-1]:
        row.append(entry)

    Warehouse.append(row)

Password = 0
index = 0 
while True:
    for_removal = []
    for Y, row in enumerate(Warehouse):
        for X, entry in enumerate(row):
            neighbours = 0
            if entry == '@':
                start_of_Y_range = int(Y - math.ceil(Y/len(Warehouse)))
                end_of_Y_range = int(Y + 2 - math.floor( Y/(len(Warehouse) - 1) ))
                start_of_X_range = int(X - math.ceil(X/len(row)))
                end_of_X_range = int(X + 2 - math.floor( X/(len(row) - 1) ))
                for i in range(start_of_Y_range, end_of_Y_range):
                    for j in range(start_of_X_range, end_of_X_range):
                        if Warehouse[i][j] == '@':
                            neighbours +=1
                
                neighbours -= 1
                if neighbours < 4:
                    Password += 1
                    for_removal.append([Y,X])

    if not len(for_removal):
        break

    for Y,X in for_removal:
        Warehouse[Y][X] = '.'
    
    index += 1

    


print(Password)