import numpy as np

f = open("InputDay6.txt", 'r')

problems = []
Password = 0
for line in f:
    problems.append(line[:-1])

#Initialize rotated matrix
rotated_pr = []
i = 0
while i < len(problems[0]):
    j = 0
    temp = []
    while j < len(problems):
        temp.append("")
        j += 1
    
    rotated_pr.append(temp)
    i += 1

# Rotate problems matrix, For better legibility and for my sanity
i = 0
while i < len(problems):
    j = 0
    while j < len(problems[0]):
        rotated_pr[j][len(problems)-1-i] = problems[i][j]
        j += 1
    i += 1


Password = 0
Y = 0
Off_range = True
temp_Password = 0
while Y < len(rotated_pr):

    # I am taking advantage of the fact that the operator is in the same column as the first digit of the largest number
    # As well as the fact that there is only one column of spaces between the groups
    numbers = rotated_pr[Y]
    numbers = numbers[::-1]

    # Initialize temp_Password
    if Off_range:
        if numbers[-1] == "*":
            temp_Password = 1
            operation = "*"
        else:
            temp_Password = 0
            operation = "+"

    # Check if we are moving to the next group of numbers
    Off_range = True
    for character in numbers:
        if character != " ":
            Off_range = False
            break


    if not Off_range:
        # Initialize the number building
        temp = 0
        # Remove the last column which either has the operator or empty space
        numbers = numbers[:-1]
        # Build the number, taking advantage of the fact that there are no spaces in the middle of the number (counting as zeroes)
        X = 0
        while X < len(rotated_pr[Y])-1:
            if numbers[X] != " ":
                temp = temp * 10 + int(numbers[X])
            X += 1
        
        # Build the sum/product of the line
        # print(temp)
        if operation == "*":
            temp_Password *= temp
        else:
            temp_Password += temp
        

    # If we are about to move into the next block, add the product/sum to the Password
    if Off_range:
        # print(temp_Password)
        Password += temp_Password
    Y += 1

# Adding the last line since it doesn't end with spaces to get off range and I am too lazy to pad
Password += temp_Password
print(Password)