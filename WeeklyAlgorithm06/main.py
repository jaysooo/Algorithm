
inputT=int(input())
t=0
cnt=0
def solution(n,inc):
    global cnt
    n=inc+n

    if n>t:
        return 0

    if n==t:
        cnt+=1
        return 0

    return solution(n,1)+solution(n,2)+solution(n,3)

for i in range(0,inputT):
    cnt=0
    t=int(input())
    solution(0,0)
    print(cnt)

