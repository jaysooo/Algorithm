import math

def solution():
    hits = [0]* 10
    N = input()
    # set number count
    for c in N:
        if c == '9':
            c = 6
        idx = int(c)
        hits[idx] +=1
        
    hits[6] = math.ceil(hits[6]/2)    
    print(max(hits))
    
solution()