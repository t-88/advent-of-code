

pairArr = []


fileName = "input.txt"
with open(fileName,"r") as f:
    for line in f:
        line = line.strip()
        pairs = line.split(",")
        pair = []
        for i in pairs:
            pair.append(list(map(int,i.split("-"))))
        pairArr.append(pair)

def boundry_check(a,b):
    return b[0] <= a[0] and a[len(a) - 1] <= b[len(b) - 1]


counter = 0
for pair in pairArr:
    if(boundry_check(pair[0],pair[1]) or boundry_check(pair[1],pair[0])):
        counter += 1

print(counter)