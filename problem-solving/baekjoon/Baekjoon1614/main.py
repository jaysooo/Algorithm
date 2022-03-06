import sys
input = sys.stdin.readline

def set_test_case():
    F = int(input())
    M = int(input())
    return F,M

def solution():
    F,M = set_test_case()
    result = 0 

    if F==1:
        result = 8*M
    elif F==5:
        result = 8 * M +4
    else:
        if M % 2 == 0 :
            result = 4 * M + (F-1)
        else:
            result = 4 * M + (5-F)
            
    print(result)
            
if __name__=='__main__':
    solution()