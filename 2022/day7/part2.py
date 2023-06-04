import sys

def end(arr):
    return len(arr) == 0

sys.setrecursionlimit(2000)
fileName = "input.txt"

lines = []
with open(fileName,"r") as f:
    for line in f:
        lines.append(line.strip())
fileSys = {}


def map_file_sys(lines,i,depth,path):
    if i >= len(lines):
        return []
    line = lines[i].split()
    if(len(line) == 3):
        if(line[1] == "cd"):
            if(line[2] == ".."):
                if len(path): 
                    path.pop()
                map_file_sys(lines, i + 1,depth - 1,path)
            else:
                path.append(line[2])
                map_file_sys(lines, i + 1,depth + 1,path)
    elif line[1] == "ls":
        map_file_sys(lines, i + 1, depth,path)
    else:
        if "->".join(path) not in fileSys:
            fileSys["->".join(path)] = []

        if(line[0] == "dir"):
            a = list(path)
            a.append(line[1])
            fileSys["->".join(path)].append("->".join(a))
        else:
            fileSys["->".join(path)].append(int(line[0]))

        map_file_sys(lines,i+1,depth,path)
def parse_all(root,i):
    if i >= len(root):
        return 0
    if(type(root[i]) == str):
        sum = parse_all(fileSys[root[i]],0) 
        root[i] = sum
        return sum +  parse_all(root,i + 1)
    return root[i] + parse_all(root,i + 1)
       
map_file_sys(lines, 0,-1,[])
spaceNeeded = 30000000 - (70_000_000 - parse_all(fileSys["/"],0))
bestMin = 70_000_000

for key in list(fileSys.keys()):
    # i calculate the sum of every dir
    fileSys[key] = sum(fileSys[key])
    # i check if its bigger then spaceNeeded
    # and its lesser then the best min i found
    if bestMin > fileSys[key] and fileSys[key] >= spaceNeeded:
        bestMin = fileSys[key]

print(bestMin)

    