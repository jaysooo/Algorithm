import itertools
import sys
input = sys.stdin.readline

# variables for backtracking
VISIT = []
M = []
STACK = []
N = 0 
MIN_SCORE = 100


def set_test_case():
    M = []
    N = int(input())
    for i in range(0,N):
        line  = input().split(' ')
        x = list(map(lambda x: int(x),line))
        M += [x]
        
    return M,N


# return Score difference of Two Team
def comparison_team(A,B,M):
    A_score=  0 
    B_score = 0 
    for i in A:
        DIFF = set(A)- set ([i])
        for j in DIFF:    
            A_score += M[i][j]
    for i in B:
        DIFF = set(B)- set ([i])
        for j in DIFF:   
            B_score += M[i][j]
    return abs(A_score - B_score)



def dfs(depth,member_idx):
    global VISIT,M,N,MIN_SCORE,STACK

    # return condition
    if depth == (N//2):
        A = []
        B = []
        for i, v in enumerate(VISIT):
            if v :
                A +=[i]
            else:
                B +=[i]
        score = comparison_team(A,B,M)
        if MIN_SCORE > score:
            MIN_SCORE = score
        return 0

    for i in range(member_idx+1,N):
        VISIT[i] = True
        dfs(depth+1,i)
        VISIT[i]=False
    
    return 0 
            
# backtracking method
def solution2():
    global VISIT,M,N,MIN_SCORE,STACK
    M,N = set_test_case()
    VISIT =[False]* N
    MIN_SCORE = 100 
    dfs(0,-1)
    print(MIN_SCORE)


# simple method
def solution():
    # M = score map , N = Soccer member count
    M,N = set_test_case()
    member = [x for x in range(0,N)]

    combi_member = list(itertools.combinations(member,N//2))
    score = 100
    for case in combi_member:
        # two team
        A=[]
        B=[]
        team_bit_map = [False] * N
        
        # Divid team 
        for i in case:
            team_bit_map[i]=True
            A += [i]
        
        for i,v in enumerate(team_bit_map):
            if v == False:
                B += [i]
    
        # score calculate
        local_score = comparison_team(A,B,M)

        if score > local_score :
            score = local_score
    # answer 
    print(score)

def main():
    solution2()
    
if __name__ == '__main__':
    main()