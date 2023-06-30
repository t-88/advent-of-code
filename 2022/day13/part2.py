from part1 import Part1
from ast import literal_eval

if __name__ == "__main__": 
    lines = []
    
    with open("input.txt","r") as f:
        for line in f:
            if line.strip():
                lines.append(literal_eval(line))
    p1 = Part1()
    lines.append([[2]])
    lines.append([[6]])


    for i in range(len(lines) - 1):
        for j in range(i,len(lines)):
            if p1.compare(lines[j],lines[i]):
                lines[j] , lines[i] = lines[i],lines[j]
    print((lines.index([[2]]) + 1) * ((lines.index([[6]]) + 1))) 