

# 0 right
# 1 down
# 2 left
# 3 up
#testC=[[1,2,3],[4,5,6],[7,8,9]]
testC=[[1,2,3],[8,9,4],[7,6,5]]
seq=[]
N=3
M=3

markMap=[[0 for rows in range(N)]for cols in range(M)]

def updatePos(_Map,pos):
    x=pos[0]
    y=pos[1]

    if y+1 < M and markMap[x][y+1]==0:
        y=y+1
        pos[1]=y
        markMap[x][y]=1
        seq.append(testC[x][y])
    elif x+1 < N and markMap[x+1][y]==0:
        x=x+1
        pos[0]=x
        markMap[x][y]=1
        seq.append(testC[x][y])
    elif y-1 >=0 and markMap[x][y-1]==0:
        y=y-1
        pos[1]=y
        markMap[x][y]=1
        seq.append(testC[x][y])
    elif x-1>=0 and markMap[x-1][y]==0:
        x=x-1
        pos[0]=x
        markMap[x][y]=1
        seq.append(testC[x][y])
    else:
        pos[0]=-1

    
    return pos



def solution():
    roundMap(testC)
    print(seq)

def roundMap(_map):
    currentPos=[0,-1]
    while(True):
        currentPos=updatePos(_map,currentPos)
        if currentPos[0]==-1:
            break
 


#for i in range(0,N):
#    for j in range(0,M):

        

solution()