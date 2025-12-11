# The best way would probably be to find the are covered by the polygon and compare it against  the ideal are of the square. Can't think of the eq/method to calculate it now so plan B is below
f = open("InputDay9.txt",'r')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def Area(tileA, tileB):

    Xa,Ya = tileA
    Xb,Yb = tileB

    return (abs(Xa - Xb) + 1) * (abs(Ya - Yb) + 1)

# The idea is to check if any line passes through the virtual box created by the two corners. If a line passes through then a portion of it must be outside of the polygon
def Validity(Tiles, index_1, index_2, Graph):

    Xa, Ya = Tiles[index_1]
    Xb, Yb = Tiles[index_2]

    if Xa < Xb:
        range_X = range(Xa+1,Xb)
    else:
        range_X = range(Xb+1,Xa)

    if Ya < Yb:
        range_Y = range(Ya+1,Yb)
    else:
        range_Y = range(Yb+1,Ya)

    a = Graph
    while True:
        Xc, Yc = a.data
        Xd, Yd = a.next.data

        if Xc < Xd:
            range_Xb = range(Xc+1,Xd)
        else:
            range_Xb = range(Xd+1,Xc)

        if Yc < Yd:
            range_Yb = range(Yc+1,Yd)
        else:
            range_Yb = range(Yd+1,Yc)

        if Xc == Xd:
            if Xc in range_X:
                if not (range_Y.start > (range_Yb.stop-1)) and not(range_Yb.start > (range_Y.stop-1)):
                    return False
        elif Yc == Yd:
            if Yc in range_Y:
                if not (range_X.start > (range_Xb.stop-1)) and not (range_Xb.start > (range_X.stop-1)):
                    return False

        

        a = a.next
        if a == Graph:
            break

    return True

# Checks if the box is outside of the polygon by counting the number of lines preceding it ( requires filtering out boxes that are half in half out )
def Filter_out_boxes(combs, graph, Tiles):

    temp = {}
    for box in combs:
        index_a, index_b = box
        Xa, Ya = Tiles[index_a]
        Xb, Yb = Tiles[index_b]

        middle_X = (Xa + Xb) //2
        floor_Y = Ya if Ya < Yb else Yb

        a = graph
        count = 0
        while True:

            if a.data[0] == a.next.data[0]:
                a = a.next
                continue
            if (a.data[0] <= middle_X and a.next.data[0] > middle_X) or (a.next.data[0] <= middle_X and a.data[0] > middle_X):
                if a.data[1] <= floor_Y:
                    count +=1

            
            a = a.next
            # a = a.next
            if a == graph:
                break

        if count % 2 == 1:
            temp[box] = combs[box]

    
    return temp


Red_tiles = []
for line in f:
    line = line[:-1]
    X,Y = line.split(",")
    X = int(X)
    Y = int(Y)

    Red_tiles.append([X,Y])
print("Red_Tiles")

# Construct graph
First_tile = Node(Red_tiles[0])
n = First_tile
for tile in Red_tiles[1:]:
    temp = Node(tile)
    n.next = temp

    n = temp

n.next = First_tile
print("Graph")


Area_combs = {}
for index, box in enumerate(Red_tiles):
    i = index + 1
    while i < len(Red_tiles):
        if Validity(Red_tiles,index,i,First_tile):
            Area_combs[(index,i)] = Area(box, Red_tiles[i])
        i += 1

print("Area")
sorted_Area_combs = {k: v for k, v in sorted(Area_combs.items(), key=lambda item: item[1], reverse=True)}

s = Filter_out_boxes(sorted_Area_combs, First_tile, Red_tiles)
for i in s:
    print(sorted_Area_combs[i])
    break