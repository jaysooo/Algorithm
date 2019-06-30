
testCase=int(input())


def solution(n):
    x=int(n/5)

    for i in range (x,-1,-1):
        y=n-(i*5)
        if y%3==0:
            return i+(y/3)
    
    return -1

print(solution(testCase))