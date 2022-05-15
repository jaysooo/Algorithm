import sys
input = sys.stdin.readline


# Ti = 처리시간
# Si = 마감시각

# Idea) 끝의 마감시각부터 처리시간을 빼가면서, 일 시작시각을 계산한다.

# 1) 마감시각 기준 정렬 
# 2) 일 업무(테스트 케이스)별로, 일 시작 시각 계산.

# 	prev_Si = 이전 업무 시작 시각 기준으로 처리하되 현재 마감 시각보다 크면 값 갱신: 마감시각 - 처리시각 

# 	IF prev_Si > Si:
# 		prev_Si = Si
# 	prev_Si -= Si 

def set_test_case():
    N =  int(input())
    N_CASE=[]
    
    for i in range(0,N):
        case = input().split(" ")
        set_case = (int(case[0]),int(case[1]))
        N_CASE.append(set_case)
    N_CASE.sort(key = lambda x : x[1],reverse=True)
    return N_CASE

def solution():
    work_array = set_test_case()
    prev_Si = work_array[0][1]
    for Si,Ti in work_array:
        if prev_Si > Ti :
            prev_Si = Ti
        prev_Si = prev_Si - Si

    if prev_Si < 0:
        prev_Si = -1

    print(prev_Si)
    
solution()