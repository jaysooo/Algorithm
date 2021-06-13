import sys

def inputCase():
    N,Q = sys.stdin.readline().split(' ')
    N,Q  = int(N),int(Q)
    ducks = []
    for i in range(0,Q):
        ducks.append(int(sys.stdin.readline()))

    return N,Q,ducks

def getParentNode(childNode):
    return (childNode)//2
        
def solution():
    # 입력 전처리
    N,Q,ducks = inputCase()

    BT_F = [False for x in range(0,N+1)] # 이진 트리 배열, 오리의 땅의 점유 여부를 체크

    for e in ducks:
        p = e
        hasLand = False
        preDuckLoc = 0
        
        while(p>1):

            if BT_F[p] == True:
               hasLand = Tru신
               preDuckLoc = p
            
            p = getParentNode(p) # 부모 노드 갱신

        if hasLand:
            print(preDuckLoc)
        else:
            print(preDuckLoc)
            BT_F[e]=True


solution()
