# X => loss| Y => draw| Z => win

def round_score(round):
    round[0] = (ord(round[0]) - ord("A")) 
    score = (ord(round[1]) - ord("X")) * 3
    if(score == 3):
        return  score + round[0]
    elif score == 6:
        # 0 < 1; 1 < 2 ; 2 < 0
        return  score + (0 if round[0] == 2 else round[0] + 1) 
    
    # 0 < 1; 1 < 2 ; 2 < 0
    return  score + (2 if round[0] == 0 else round[0] - 1) 

total_sum = 0
with open("input.txt","r") as f:
    for line in f:
        round = line.strip().split(" ")
        total_sum += round_score(round) + 1 

print(f"total: {total_sum}")
