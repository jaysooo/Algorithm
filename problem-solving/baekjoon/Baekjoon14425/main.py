import sys

input = sys.stdin.readline

def set_test_case():
    input_str = input().split()
    N,M = int(input_str[0]),int(input_str[1])
    S = {}
    case = []


    for i in range(0,N):
        word = input()
        S[word] = True 
    
    for i in range(0,M):
        word = input()
        case += [word]
    
    return S,case

def solution():
    S,M = set_test_case()
    count = 0
    
    for word in M:
        if word in S:
            count +=1
            
    print(count)

    
solution()
        
        
        
