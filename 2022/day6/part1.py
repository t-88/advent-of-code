fileName = "input.txt"

line = ""
with open(fileName,"r") as f:
    line = f.readline()

steam = [line[i] for i in range(3)]
for i in range(3,len(line)):
    # if charrepeated char pop and continue
    steam.append(line[i])
    if len(set(steam)) != len(steam):
        steam.pop(0)
    else:
        break
    

# offset by 1
print(i + 1)     
