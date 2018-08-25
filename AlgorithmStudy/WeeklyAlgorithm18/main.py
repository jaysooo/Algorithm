import string

N=11
K=1

def check(n,k):

    cnt=0
    for i in range(1,n+1):
        tmp=str(i)

        for j in range(0,len(tmp)):
            if tmp[j]==str(k):
                cnt+=1
                #print(tmp)
    
    print(cnt)

def solution(n,k):
    a1=1
    m=int(len(str(n))-1)
    print(m)
    a2=a1*m+10*m
    
    

check(N,K)
solution(N,K)