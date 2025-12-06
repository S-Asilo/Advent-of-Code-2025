f = open("InputDay6.txt", 'r')

problems = []
Password = 0
for line in f:
    line = line[:-1].split()
    if not len(problems):
        for index, element in enumerate(line):            
            problems.append([int(element),int(element)])
    else:
        for index, element in enumerate(line):
            if element == '+':
                Password += problems[index][0]
                continue
            elif  element == '*':
                Password += problems[index][1]
                continue
            problems[index][0] += int(element)
            problems[index][1] *= int(element)

print(Password)
