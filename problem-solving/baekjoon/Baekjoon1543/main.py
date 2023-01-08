import sys

input = sys.stdin.readline


def set_test_case():
    base_str = input()[:-1]
    match_str = input()[:-1]
    return base_str,match_str

def solution():
    S , M = set_test_case()  


    cnt = 0 
    index = 0
    while(len(S)> 0 and index >=0 ):
        index = S.find(M)
        if index >= 0 :
            cnt += 1
            S = S[index+len(M):]

    print(cnt)
    

        

solution()