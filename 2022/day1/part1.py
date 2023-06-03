


elfs = [0]

with open("input.txt","r") as f:
    for line in f:
        if(line != "" and line != "\n"):
            elfs[len(elfs) - 1] += int(line)
        else:
            elfs.append(0)


index = elfs.index(max(elfs))  + 1
print(f"elf id: {index}, calories {elfs[index - 1]}")