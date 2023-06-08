def file_to_arr(fileName,func=lambda x : x ):
    out = [] 
    with open(fileName,"r") as f:
        out.append(func(f.readline()))
    return out