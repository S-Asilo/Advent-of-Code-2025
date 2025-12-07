f = open("InputDay7.txt", "r")

# Password = 1
index = {}
for i, line in enumerate(f):
    if i == 0:
        index[line.index('S')] = 1
    else:
        if line.find('^') == -1:
            continue
        else:
            temp = {}
            for el in index:
                if line[el] == '^':
                    # Check if it's a new entry or update value
                    try:
                        temp[el-1] = temp[el-1] + index[el]
                    except:
                        temp[el-1] = index[el]

                    try:
                        temp[el+1] = temp[el+1] + index[el]
                    except:
                        temp[el+1] = index[el]
                else:
                    # Probably unecessary 
                    try:
                        temp[el] = temp[el] + index[el]
                    except:
                        temp[el] = index[el]
            index = temp.copy()

Password = 0
for i in index:
    Password += index[i]
print(Password)