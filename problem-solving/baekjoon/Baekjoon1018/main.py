

#testCase = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','B','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
#testCase = [['B','B','B','B','B','B','B','B','W','B','W','B','W'],['B','B','B','B','B','B','B','B','B','W','B','W','B'],['B','B','B','B','B','B','B','B','W','B','W','B','W'],['B','B','B','B','B','B','B','B','B','W','B','W','B'],['B','B','B','B','B','B','B','B','W','B','W','B','W'],['B','B','B','B','B','B','B','B','B','W','B','W','B'],['B','B','B','B','B','B','B','B','W','B','W','B','W'],['B','B','B','B','B','B','B','B','B','W','B','W','B'],['W','W','W','W','W','W','W','W','W','W','B','W','B'],['W','W','W','W','W','W','W','W','W','W','B','W','B']]
#tmpMap = [['W','W','W','W','W','W','W','B'],['W','B','B','B','B','B','B','B'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
#N=8
#M=8
inputStr=raw_input().split(' ')
N=int(inputStr[0])
M=int(inputStr[1])

tmpMap=[]
for i in range(0,N):
    tmp=raw_input()
    tmpMap.append(list(tmp))

minCnt=32

def checkIsVaild2(chessMap):
    global minCnt
    cnt=0
    for i in chessMap:
        l=len(i)
        j=1
        while(j<l):
            if (ord(i[j])+ord(i[j-1])!=153):
                cnt+=1
                if minCnt<cnt:
                    return
            j+=2
    #print(cnt)
    if minCnt>cnt:
        minCnt=cnt
            

def checkIsValid(chessMap):
    global minCnt
    block=['','W','B']
    fixMap=64
    cur=1
    cnt=0
    for i in chessMap:
        for j in i:
            cur=cur*-1
            if j==block[cur]:
                cnt+=1
        cur=cur*-1

    cnt=fixMap-cnt
    if minCnt>cnt:
        minCnt=cnt

    cnt=0
    cur=-1
    for i in chessMap:
        for j in i:
            cur=cur*-1
            if j==block[cur]:
                cnt+=1
        cur=cur*-1

    cnt=fixMap-cnt

    if minCnt>cnt:
        minCnt=cnt

    #print(cnt)
    
def solution(_input,N,M):

    for col in range(0,N-7):
        for row in range(0,M-7):
            slice = [_input[i][row:row+8] for i in range(col,col+8)]
            #print(slice)
            checkIsValid(slice)

    print(minCnt)

solution(tmpMap,N,M)