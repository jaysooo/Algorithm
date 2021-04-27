
def inputCase():
    N,M,L = [int(x) for x in input().split(" ")]
    S = []
    Q = []
    for i in range (0,M):
        S.append(int(input()))
    
    for i in range(0,N):
        Q.append(int(input()))
    
    return N,M,L,S,Q



def optimalSplit(maxCakeSize,cakePiece,cake):
	preCake=0

	for c in cake:
		if (c - preCake ) >= maxCakeSize:
			cakePiece -=1
			preCake = c 
	
	if cakePiece > 0 :
		return True
	else:
		return False
def cakeSplit(S,M,L,splitNumber):
    startPos = 1
    splitNumber+=1
    endPos = L
    MaxMid = 0 
    mid = (startPos+endPos)//2

    while(startPos<=endPos):
        if optimalSplit(mid,splitNumber,S):
            # 줄이는 로직 -> 왼 쪽 파티션으로 이동
            endPos=mid-1
        else:
            # 늘리는 로직 -> 오른쪽 파티션으로 이동
            startPos=mid+1
        mid = (startPos+endPos)//2
         
    print(mid)


def main():
    N,M,L,S,Q = inputCase()
    #N,M,L,S,Q = 2,5,70,[10,20,35,55,60],[3,4]
    S.append(L)
    for q in Q:
        cakeSplit(S,M,L,q)

if __name__=="__main__":
    main()

