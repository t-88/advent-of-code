
rockes = []
min_x , max_x , min_y , max_y = float("inf"),float("-inf"),float("inf"),float("-inf")
with open("input.txt","r") as f:
    for line in f:
        line = line.strip()
        lines = line.split("->")   
        for l in range(len(lines) - 1):
            
            r1 = list(map(int,lines[l].split(",")))
            r2 = list(map(int,lines[l+1].split(",")))

            min_x = min(min_x,r1[0],r2[0])
            max_x = max(max_x,r1[0],r2[0])

            min_y = min(min_y,r1[1],r2[1])
            max_y = max(max_y,r1[1],r2[1])


            rockes.append([(r1[0],r1[1]),(r2[0],r2[1])])


def inline(line,point):
    return (min(line[0][0],line[1][0]) <= point[0] and point[0] <= max(line[0][0],line[1][0]) and min(line[0][1],line[1][1]) <= point[1] and point[1] <= max(line[0][1],line[1][1]))
def collided(rockes,sand,point):
    #      point (x,y)
    # rock line (x1,y1) (x2,y2)
    # y = a * x + b

    if point[1] == max_y + 2:
        return 1    

    for s in sand:
        if point == s:
            return 2
    for rock in rockes:
        if not inline(rock,point):
            # print(0rock[0][0],rock[1][0])
            continue

        a = 0
            
        if rock[0][0] - rock[1][0] == 0:
            a = float("inf")

        elif rock[0][1] - rock[1][1] != 0:
            a = (rock[0][1] - rock[1][1]) / (rock[0][0] - rock[1][0])
        b = rock[0][1] - a * rock[0][0] 

        if a == float("inf"): 
            if point[0] == rock[0][0]:
                return True
        elif a * point[0] + b == point[1]:
            return 1

    return 0
sand = []


# print map
# for y in range(max_y + 1):
#     for x in range(min_x,max_x + 1):
#         # if point[0] == x and point[1] == y:
#             # print("o",end="")
#         if collided(rockes,sand,(x,y)) == 1:
#             print("#",end="")
#         elif collided(rockes,sand,(x,y)) == 2:
#             print("o",end="")
#         else:
#             print(".",end="")
#     print()

done = False
while True:
    point = (500,0)
    rested = False
    while not rested:
        if collided(rockes,  sand,(point[0],point[1]+1)) == 0:
            point = (point[0],point[1]+1)
        elif collided(rockes,sand,(point[0]-1,point[1]+1)) == 0:
            point = (point[0]-1,point[1]+1)
        elif collided(rockes,sand,(point[0]+1,point[1]+1)) == 0:
            point = (point[0]+1,point[1]+1)
        else:
            rested = True
        
    sand.append(tuple(point))
    print(len(sand))
    if point == (500,0):
        break



print(len(sand))