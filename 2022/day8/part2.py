import filifed


# read file
grid = filifed.file_to_arr(
                            "input.txt",
                            lambda line: 
                            [int(chr) for chr in line.strip()]
                           )

# print grid
for line in grid:
    print(line)

cols , rows = len(grid[0]) , len(grid)

# flatten grid
tmp = []
for line in grid:
    for num in line:
        tmp.append(num)
grid = tmp


# remap coords
def get_val(x,y):
    return grid[y * cols + x]
# do check
def scenic_score(x,y):
    curr = get_val(x,y)
    score = []

    counter = 1
    biggest = get_val(x + 1,y) 
    for i in range(x + 2,rows):
        if (biggest <= get_val(i,y)):
            biggest = get_val(i,y)
            counter += 1
        if(curr <= get_val(i,y)):
            break

    score.append(counter)
    biggest = get_val(x-1 ,y) 
    counter = 1
    for i in range(x - 2,-1,-1):
        if(biggest <= get_val(i,y)):
            biggest = get_val(i,y)
            counter += 1

        if(curr <= get_val(i,y)):
            break
    score.append(counter)
    counter = 1
    biggest = get_val(x ,y + 1) 
    for i in range(y + 2,cols):
        if (biggest <= get_val(i,y)):
            biggest = get_val(i,y)
            counter += 1            
        if(curr <= get_val(x,i) ):
            break
    score.append(counter)
    counter = 1
    biggest = get_val(x ,y - 1) 
    for i in range(y - 2,-1, -1):
        if (biggest <= get_val(i,y)):
            biggest = get_val(i,y)
            counter += 1            

        if(curr <= get_val(x,i) ):
            break

    score.append(counter)

    counter = 1
    for i in score:
        counter *= i
    return  (counter,score)


best = 0

for y in range(1 ,rows - 1):
    for x in range(1 ,cols - 1):
        (curr,_) = scenic_score(x,y)
        if curr > best:
            print(scenic_score(x,y),x,y)
            best = curr
print(best)
