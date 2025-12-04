f = open("InputDay1.txt", "r")

Weight = {'R':1, 'L':-1}

Password = 0
Position = 50
for line in f:
    direction = line[0]
    steps = int(line[1:])

    # This is to take into account the steps larger than 100 ( they definitely pass over 0 )
    Password += steps // 100 

    old_Position = Position
    Position = (Position + steps * Weight[direction]) % 100

    if old_Position == 0:
        continue
    elif ((Position - old_Position) * Weight[direction]) < 0:
        Password += 1
    elif Position == 0 and old_Position != 0:
        Password +=1

print(Password)