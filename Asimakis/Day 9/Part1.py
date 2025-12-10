f = open("InputDay9.txt",'r')


def Area(tileA, tileB):

    Xa,Ya = tileA
    Xb,Yb = tileB

    return (abs(Xa - Xb) + 1) * (abs(Ya - Yb) + 1)

Red_tiles = []
for line in f:
    line = line[:-1]
    X,Y = line.split(",")
    X = int(X)
    Y = int(Y)

    Red_tiles.append([X,Y])


Area_combs = {}
for index, box in enumerate(Red_tiles):
    i = index + 1
    while i < len(Red_tiles):
        Area_combs[(index,i)] = Area(box, Red_tiles[i])

        i += 1

sorted_Area_combs = {k: v for k, v in sorted(Area_combs.items(), key=lambda item: item[1], reverse=True)}
# print(sorted_Area_combs)

for i in sorted_Area_combs:
    print(sorted_Area_combs[i])
    break