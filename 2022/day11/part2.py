import sys
sys.path.append("../")
import filified

lines = filified.file_to_arr("input.txt")
ops = {
    "*" : lambda x , y, div : (x * y , True),
    "+" : lambda x , y, div : (x + y , True),
}


currMonky = -1
monkies = []
for line in lines:
    if line.find("Monkey") != -1:
        currMonky += 1
        monkies.append( {})
    elif line.find("Starting") != -1:
        line = list(map(int,line.replace("Starting items:","").replace(",","").strip().split(" ")))
        monkies[currMonky]["items"] = line
        monkies[currMonky]["times"] = 0
    elif line.find("Operation:") != -1:
        line = line.replace("Operation: new = old","").strip().split(" ")
        monkies[currMonky]["op"] = line
    elif line.find("Test:") != -1:
        line = int(line.replace("Test: divisible by ","").strip().split(" ")[0])
        monkies[currMonky]["div"] = line
    elif line.find("If true:") != -1:
        line = int(line.replace("If true: throw to monkey ","").strip().split(" ")[0])
        monkies[currMonky]["True"] = line
    elif line.find("If false:") != -1:
        line = int(line.replace("If false: throw to monkey ","").strip().split(" ")[0])
        monkies[currMonky]["False"] = line
         

for round in range(1000):
    for monky in monkies:
        monky["times"] += len(monky["items"])
        for i in range(len(monky["items"])-1,-1,-1):
            value  = int(monky["items"].pop(i))
            num = int(value) if monky["op"][1] == "old" else int(monky["op"][1]) 
            (value , isTrue) = ops[monky["op"][0]](value,num,monky["div"])

            monkies[monky[ "True" if isTrue else "False" ]]["items"].append(value)
            
    print(round)
for i,monky in enumerate(monkies):
    print(f"Monkey {i} inspected items {monky['times']} times.")

