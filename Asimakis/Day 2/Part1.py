f = open("InputDay2.txt", "r")

for line in f:
    line = line.split(",")

    Password = 0
    for ranges in line:
        ranges = ranges.split("-")
        beginning = ranges[0]
        ending = ranges[1]

        for i in range(int(beginning),int(ending)+1):
            number = str(i)
            if len(number) % 2 == 0:
                offset = 0
                second_half = len(number) // 2
                invalid_ID = False
                while offset < second_half:
                    if number[offset] != number[second_half + offset]:
                        invalid_ID = True
                        break

                    offset += 1

                if not invalid_ID:
                    Password += i
    

print(Password)