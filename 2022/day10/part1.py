import sys
sys.path.append("../")
from filified import *

ops = file_to_arr("input.txt",lambda x: x.strip())




x = 1
cycle = 1
la_somme = 0
wanted = [20,60,100,140,180,220]
for idx , op in enumerate(ops):
    if op.find("noop") != -1:
        if cycle in wanted:
            la_somme += cycle * x
            print(cycle,idx,x,x*cycle)
        cycle += 1
    else:
        for _ in range(2):
            if cycle in wanted:
                la_somme += cycle * x    
                print(cycle,idx,x,x*cycle)
            cycle += 1
        x += int(op.split(" ")[1])

print(x,la_somme)



