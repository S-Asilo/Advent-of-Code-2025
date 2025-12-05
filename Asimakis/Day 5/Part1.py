f = open("InputDay5.txt", "r")

in_ranges = True
set_of_fresh_ingredients = []
Password = 0
for line in f:
    if len(line) == 1:
        in_ranges = False
        continue
    
    if in_ranges:
        start_of_range, end_of_range = line[:-1].split("-")
        start_of_range = int(start_of_range)
        end_of_range = int(end_of_range)
        set_of_fresh_ingredients.append(range(start_of_range, end_of_range+1))
    else:
        ingr = line[:-1]
        ingr = int(ingr)
        # print(ingr)
        for i in set_of_fresh_ingredients:
            if ingr in i:
                Password += 1
                break
    
print(Password)