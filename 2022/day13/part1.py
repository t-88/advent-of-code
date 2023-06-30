from ast import literal_eval


class Part1:
    def __init__(self):
        pass

    def compare(self,l1,l2):
        for i1 in range(max(len(l1),len(l2))):
            if i1 == len(l1) and  i1 == len(l2):
                return "TBD"
            if i1 >= len(l1):
                return True
            elif i1 >= len(l2):
                return False
            
            if type(l1[i1]) != type(l2[i1]):
                res = ""
                if type(l1[i1]) == int:
                    res = self.compare([l1[i1]],l2[i1])
                else:
                    res = self.compare(l1[i1],[l2[i1]])
                
                if res != "TBD":
                    return res
            else:
                if type(l1[i1]) == int:
                    if l1[i1] < l2[i1]:
                        return True
                    elif l1[i1] > l2[i1]:
                        return False
                
                else:

                    res = ""
                    res = self.compare(l1[i1],l2[i1])
                    if res != "TBD":
                        return res
        return "TBD"


if __name__ == "__main__": 

    lines = []

    with open("input.txt","r") as f:
        for line in f:
            if line.strip():
                lines.append(literal_eval(line))

    p1 = Part1()
    sum = 0
    for i in range(len(lines)//2):
        if p1.compare(lines[2*i + 0],lines[2*i +1]):
            sum += i + 1 
    print(sum)
