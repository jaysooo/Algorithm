


def estimateMaxN(items,n):
    return int(sum(items)/n)

def calcularteN(items,widthN,N):
    cnt=0
    for i in items:
        cnt+=int(i/widthN)

    if cnt == N:
        return True
    else:
        return False

def adjustMaxN(items,estimatedN,N):
    e_N=estimatedN
    while True:
        res = calcularteN(items,e_N,N)
        if res:
            break
        e_N-=1
    return e_N
    
def solution():
   # K=4
    #N=11
    K,N=input().split(' ')
    K=int(K)
    N=int(N)
    k_items=[]
    for i in range(0,K):
        k_items+=[int(input())]
    #k_items=[802,743,457,539]
    print(adjustMaxN(k_items,estimateMaxN(k_items,N),N))


solution()