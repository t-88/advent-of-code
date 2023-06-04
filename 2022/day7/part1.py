import sys

def end(arr):
    return len(arr) == 0

# solving it recursivty bc fuck yeah
# setuping up the recursivty 
sys.setrecursionlimit(2000)
fileName = "input.txt"

lines = []
with open(fileName,"r") as f:
    for line in f:
        lines.append(line.strip())
fileSys = {}


# parsing the file sys using path i did it using ids it didnt work
# i got the idea of using the whole path from https://www.youtube.com/watch?v=YLHPABNNgZU&ab_channel=WilliamY.Feng
# not to say i understood his answer, i just heard path and i said to my self intersting
# i didnt think i would work but it did cool i guss
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
    return root[i] +parse_all(root,i + 1)
       
map_file_sys(lines, 0,-1,[])
parse_all(fileSys["/"],0)
totalSum = 0

for key in list(fileSys.keys()):
    tmp =  sum(fileSys[key])
    totalSum += 0 if tmp > 100000 else tmp


print(totalSum)
    