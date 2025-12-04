f = open("InputDay1.txt", "r")

Weight = {'R':1, 'L':-1}

Password = 0
Position = 50
for line in f:
    direction = line[0]
    steps = int(line[1:])

    Position = (Position + steps * Weight[direction]) % 100

    if Position == 0:
        Password += 1

print(Password)