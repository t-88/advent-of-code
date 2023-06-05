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
visible = len(grid[0]) * 2 + len(grid) * 2 - 4

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
def is_visible(x,y):
    curr = get_val(x,y)

    ioti = False
    for i in range(x + 1,rows):
        if(get_val(i,y) >= curr):
            ioti = True
            break
    if not ioti: return True
    ioti = False
    for i in range(0,x):
        if(get_val(i,y) >= curr):
            ioti = True
            break
    if not ioti: return True
    ioti = False
    for i in range(y + 1,cols):
        if(get_val(x,i) >= curr):
            ioti = True
            break
    if not ioti: return True
    ioti = False
    for i in range(0,y):
        if(get_val(x,i) >= curr):
            ioti = True
            break                
    
    return not ioti    


for y in range(1 ,rows - 1):
    for x in range(1 ,cols - 1):
        visible += 1 if is_visible(x,y) else 0
print(visible)