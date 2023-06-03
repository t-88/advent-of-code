# use sort 
elfs = [0]

with open("input.txt","r") as f:
    for line in f:
        if(line != "" and line != "\n"):
            elfs[len(elfs) - 1] += int(line)
        else:
            elfs.append(0)

elfs.sort(reverse=True)
print(f"total calories {sum(elfs[:3])}")