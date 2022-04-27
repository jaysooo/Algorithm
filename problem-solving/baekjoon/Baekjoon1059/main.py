
def set_test_case():
    L = int(input())
    S = input().split(" ")
    s = sorted([int(x) for x in S])
    n = int(input())
    return s,n

def solution():
    S, N = set_test_case()
    R, L = 0,0 
    for idx,va in enumerate(S):
        if va == N:
            print(0)
            return 
        if va > N and S[idx-1] < N:
            R = idx
            L = idx-1
            break
    if R > 0:
       x = ((S[R]-1) - (N-1)) * (N-S[L]) - 1
    elif L == 0 and R == 0:
        x = N * (S[R]-N) -1
    else :
        x = 0 
    print(x)
    
solution()
