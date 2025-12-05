f = open("InputDay5.txt", "r")

def comp(x):
    return x.start

in_ranges = True
set_of_fresh_ingredients = []
Password = 0
for line in f:

    subsections = []
    if len(line) == 1:
        break
    
    start_of_range, end_of_range = line[:-1].split("-")
    start_of_range = int(start_of_range)
    end_of_range = int(end_of_range)
    
    subsections.append(range(start_of_range, end_of_range+1))
    
    for i in subsections:
        flag = True
        print(subsections)
        set_of_fresh_ingredients = sorted(set_of_fresh_ingredients, key=comp)
        for r in set_of_fresh_ingredients:
            if i.start in r:
                if i.stop-1 in r:
                    flag = False
                    print("Case 0",i,r)
                    break
                else:
                    flag = False
                    print("Case 1",i,r)
                    subsections.append(range(r.stop,i.stop))
                    break
            else:
                if i.stop-1 in r:
                    flag = False
                    print("Case 2",i,r)
                    subsections.append(range(i.start,r.start))
                    break
                else:
                    if r.start in i:
                        flag = False
                        print("Case 3",i,r)
                        subsections.append(range(i.start,r.start))
                        subsections.append(range(r.stop,i.stop))
                        break
        
        if flag:
            print("Added", i)
            set_of_fresh_ingredients.append(i)
                    

print(set_of_fresh_ingredients)    
for r in set_of_fresh_ingredients:
    Password += len(r)



print(Password)