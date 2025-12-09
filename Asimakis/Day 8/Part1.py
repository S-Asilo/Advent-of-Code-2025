import math

f = open("InputDay8.txt", "r")

def distance(junction_boxA, junction_boxB):

    Xa,Ya,Za = junction_boxA
    Xb,Yb,Zb = junction_boxB

    return math.sqrt((Xa - Xb)**2 + (Ya - Yb)**2 + (Za - Zb)**2)


def Compress(C):

    while True:
        Done = True
        temp = []
        merged = False
        for index,c in enumerate(C):
            for b in C[index+1:]:
                if c.intersection(b):
                    temp.append(c.union(b))
                    merged = True
                    Done = False
                    break
            

            if not merged:
                temp.append(c)
        C = temp.copy()

        if Done:
            break
        
    return C


Junction_boxes = []
for line in f:
    line = line[:-1]
    X,Y,Z = line.split(",")
    X = int(X)
    Y = int(Y)
    Z = int(Z)

    Junction_boxes.append([X,Y,Z])


Distance_combs = {}
for index, box in enumerate(Junction_boxes):
    i = index + 1
    while i < len(Junction_boxes):
        Distance_combs[(index,i)] = distance(box, Junction_boxes[i])

        i += 1

sorted_Distance_combs = {k: v for k, v in sorted(Distance_combs.items(), key=lambda item: item[1])}

Circuits = []
Circuits.append({list(sorted_Distance_combs.keys())[0][0],list(sorted_Distance_combs.keys())[0][1]})

count = 1
print(sorted_Distance_combs)
for index in sorted_Distance_combs:
    a, b = index
    Match = False
    print(Circuits)
    Circuits = Compress(Circuits)
    print("After", Circuits)
    for circuit in Circuits:
        if a in circuit and b in circuit:
            Match = True
            break
        elif a in circuit or b in circuit:
            circuit.add(a)
            circuit.add(b)
            Match = True
            count += 1
            break
    

    if not Match:
        Circuits.append({a,b})
        count += 1


    if count == 10:
        break    

print(Circuits)