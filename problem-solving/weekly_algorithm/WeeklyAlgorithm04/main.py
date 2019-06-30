import sys

ip = int(input())

minCnt=ip
first=0
def solution(n,cnt):
    global first
    global minCnt
    cnt+=1

    if minCnt<cnt:
        return 0

    if n==1:
        if first==0:
            minCnt=cnt
            first=1
        elif minCnt >= cnt:
            minCnt=cnt
        return 0

    elif n%3==0:   
        return solution(n/3,cnt)+solution(n-1,cnt)
    elif n%2==0:
        return solution(n/2,cnt)+solution(n-1,cnt)
    else:
        return solution(n-1,cnt)
    

solution(ip,-1)
print(minCnt)


