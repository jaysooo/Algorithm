

def set_test_case():
    A = []
    B = []
    T = input() 
    for i in range(0,2):
        org = input().split(" ")
        if i == 0 :
            A = [int(x) for x in org]
        else:
            B = [int(x) for x in org]

    return A,B


def solution():
    A,B = set_test_case()
    S = 0 
    A = sorted(A)
    B_I = []
    MAP_B = {}

    for idx,va in enumerate(B):
        MAP_B[va] = idx
        
    for i in sorted(B,reverse=True):
        B_I +=[MAP_B[i]]
    
    for idx,va in enumerate(A):
        S_PART = va * B[B_I[idx]]
        S += S_PART

    print(S)



solution()