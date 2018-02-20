
inputT=int(input())
t=0
def solution(n):
    global t
    if n>t:
        return 0

    if n==t:
        return 1

    return solution(n+1)+solution(n+2)+solution(n+3)

for i in range(0,inputT):
    t=int(input()) 
    print(solution(0))