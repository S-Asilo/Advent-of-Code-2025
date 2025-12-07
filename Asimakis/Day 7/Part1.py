f = open("InputDay7.txt", "r")

Password = 0
index = set()
for i, line in enumerate(f):
    if i == 0:
        index.add(line.index('S'))
    else:
        if line.find('^') == -1:
            continue
        else:
            temp = set()
            for j, el in enumerate(index):
                if line[el] == '^':
                    Password += 1
                    temp.add(el-1)
                    temp.add(el+1)
                else:
                    temp.add(el)
            index = temp.copy()
            

print(Password)