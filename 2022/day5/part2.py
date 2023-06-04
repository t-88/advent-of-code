fileName = "input.txt"


def parse_cmd(line):
    line = line.replace("move","").replace("from","").replace("to","").strip()
    output = []
    line = line.split(" ")
    for val in line:
        if val != "" and val != "\n":
            output.append(int(val))
    return output
def parse_crate_str(crate):
    output = []
    for i in range(0,len(crate) // 4):
        output.append(crate[i * 4:(i + 1)* 4].strip().replace("[","").replace("]",""))

    return output
def arrange_crates(crates):
    output = [ [] for i in range(len(crates[0]))]
    for j in range(len(crates)):
        for i in range(len(crates[0])):
                if crates[j][i] != "":
                    output[i].insert(0,crates[j][i])

    return output 



crates = []
cmds = []

pushLines = True
with open(fileName,"r") as f:
    for line in f:
        if not pushLines:
            if len(line) > 1:
                output = parse_cmd(line)
                if len(output) > 0:
                    cmds.append(output)
        if line[:2] == " 1":
            pushLines = False
        if pushLines:
            crates.append(parse_crate_str(line))

crates = arrange_crates(crates)
for cmd in cmds:
    offset = len(crates[cmd[2] - 1])
    for i in range(cmd[0]):
        crates[cmd[2] - 1].insert(offset,crates[cmd[1] - 1].pop())

for crate in crates:
    print(crate[len(crate) - 1] , end="")

print()

