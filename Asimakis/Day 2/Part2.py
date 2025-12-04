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

            # Find divisors
            divisor = 1
            divisors = []
            while divisor <= len(number):
                if len(number) % divisor == 0:
                    divisors.append(divisor)

                divisor += 1

            divisors.pop()

            # Search for repeating patterns
            for divisor in divisors:
                offset = 0
                repetition = True
                while divisor*(offset+1) < len(number):
                    for move in range(divisor):
                        if number[(divisor*offset)+move] != number[(divisor*(offset+1))+move]:
                            repetition = False
                            break
                    
                    if not repetition:
                        break
                    offset += 1

                if repetition:
                    # print(i)
                    Password += i
                    break


    

print(Password)