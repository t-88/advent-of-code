#using a this function to calc the score of each round 
def round_score(round):
    # offseting
    round[0] = ord(round[0]) - ord("A") 
    score = ord(round[1][0]) - ord("X")  
    # giving score
    if(round[0] == score):
        score += 3
    elif((round[0] < score and not (score == 2 and round[0] == 0)) or 
                            (round[0] == 2 and score == 0)): # player won
        score += 6
    return score

total_sum = 0
with open("input.txt","r") as f:
    for line in f:
        round = line.split(" ")
        total_sum += round_score(round) + 1 

print(f"total: {total_sum}")
