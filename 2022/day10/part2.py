import sys
sys.path.append("../")
from filified import *

ops = file_to_arr("input.txt",lambda x: x.strip())


def render_screen(screen):
    for idx in range(1,len(screen)):
        print(screen[idx],end="")
        if idx % 40 == 0:
            print("")
        

screen = ["."] * 241



x = 1
cycle = 1
la_somme = 0
wanted = [20,60,100,140,180,220]
for idx , op in enumerate(ops):
    print(cycle)
    if op.find("noop") != -1:
        if x <= cycle % 40 <= x+2:
            screen[cycle] = "#"
        cycle += 1
    else:
        for _ in range(2):
            if x <= cycle % 40 <= x+2:
                screen[cycle] = "#"
            cycle += 1
        x += int(op.split(" ")[1])


render_screen(screen)
print()

