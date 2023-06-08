def file_to_arr(fileName,func=lambda x : x ):
    out = [] 
    with open(fileName,"r") as f:
        for line in f:
            out.append(func(line))
    return out