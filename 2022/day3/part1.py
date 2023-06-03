file_name = "input.txt" 

def get_shared(str1,str2):
    mapped = {} # using hash map
    output = [] 
    for char in str1: mapped[char] = 1 # mark exsisting
    for char in str2: 
        if char in mapped and  mapped[char] < 2: # make sure not to repeat
            mapped[char] += 1
            output.append(char) 
    return output

def priority(char):
    return ord(char) - ord("a") + 1 if char >= "a" else  ord(char) - ord("A") + 27

total = 0

with open(file_name,"r") as f:
    for line in f:
        line = line.strip()
        output = get_shared(line[:len(line)//2],line[len(line)//2:])

        # math
        for char in output:
            total += priority(char)

print(f"total: {total}")