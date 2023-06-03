from operator import add
file_name = "input.txt" 

# \n char fucked me pretty good, always strip ur strings :_)


def priority(char):
    return ord(char) - ord("a") + 1 if char >= "a" else  ord(char) - ord("A") + 27

# read every line
def common(lines):
    bigSum = [0] * (26 * 2)
    for line in lines:
        local = [0] * 26 * 2
        line = line.strip()
        for char in line:
            # set existing chars , dont repeat
            if(local[priority(char) - 1]) == 0: local[priority(char) - 1] = 1
        # add them in bigSum
        bigSum = list(map(add,bigSum, local))
    return bigSum.index(3) + 1

total = 0
lines = []
with open(file_name,"r") as f:
    lines = f.readlines()


total =  0
for i in range(len(lines) // 3):
    total += common(lines[i*3:(i+1)*3])

print(f"total: {total}")