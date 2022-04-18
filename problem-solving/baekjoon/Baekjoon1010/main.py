

def set_test_case():
    T = int(input())
    CASE = []
    for i in range (0,T):
        line = input().split(" ")  # 입력 문자열을 공백구분자로 분리 
        line = [int(x) for x in line]  # 연산을 위해 str -> int 형 변한
        CASE.append(line)  # 케이스들을 새로운 list 에 담음

    return CASE
        
# factorial 을 재귀로 간단히 구현
def factorial(n):
    if n <=1:
        return 1
    return n * factorial(n-1)


def solution():
    case = set_test_case() # 입력 케이스 처리 
    for i in case :
        r,n = i # 강의 서쪽은 r, 동쪽은 n 에 대입
        p = factorial(n-r) * factorial(r)  # 조합의 구한 분모 값 계산
        c = factorial(n)  # 조합의 분자 값 계산
        print(c//p) # 정답 출력 

solution()
