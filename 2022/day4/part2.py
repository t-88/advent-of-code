pairArr = []


fileName = "input.txt"
# parsing input
with open(fileName,"r") as f:
    for line in f:
        line = line.strip()
        pairs = line.split(",")
        pair = []
        for i in pairs:
            pair.append(list(map(int,i.split("-"))))
        pairArr.append(pair)

def boundry_check(a,b):
    # generate a set
    a = set([i for i in range(a[0] , a[len(a) - 1] + 1)])
    b = set([i for i in range(b[0] , b[len(b) - 1] + 1)])
    # check if there is any shared elements    
    return len(a.intersection(b)) != 0  

counter = 0
for pair in pairArr:
    # counting intersections
    if(boundry_check(pair[0],pair[1])):
        counter += 1

print(counter)