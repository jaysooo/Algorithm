#ref - https://www.acmicpc.net/problem/2133

def solution(N):
    tiles=0
    if not N%2==0:
        tiles=0
    else:
        cnt2=int(N/2)
        cnt4=N-2
        if cnt2>0:
            tiles+=pow(3,cnt2)
        tiles+=cnt4
        

    return tiles
def main():
    N=int(input())
    print(solution(N))

if __name__=='__main__':
    main()
