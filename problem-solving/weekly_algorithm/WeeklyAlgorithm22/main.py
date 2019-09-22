X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
Y = [1, 8, 9, 10, 15]


def getNextNum(arr,curPos):
    pos=0
    for i in range(curPos,len(arr)):
        if arr[i]!=0:
            pos=i
            break
    return pos

def doSortCheck(groupX):
    #check
    for i in groupX:
        print(i)


def doSortAndMerge(groupX,groupY):
    yCursor=0
    for i in range(0,len(groupX)):
        if groupX[i]==0:
            nextPos=getNextNum(groupX,i)
            if groupX[nextPos]>groupY[yCursor] or nextPos==0:
                groupX[i]=groupY[yCursor]
                yCursor+=1
            else:
                groupX[i]=groupX[nextPos]
                groupX[nextPos]=0

def doImprovedSortAndMerge(groupX,groupY):
    yCursor=0
    notEmptyCellPos=[]
    for i in range (0,len(groupX)):
        if groupX[i]!=0:
            notEmptyCellPos.append(i)

    for i in range(0,len(groupX)):
        if groupX[i]==0:
            if len(notEmptyCellPos)>0:
                nextPos=notEmptyCellPos.pop(0)
            else:
                nextPos=0
            if groupX[nextPos]>groupY[yCursor] or nextPos==0:
                groupX[i]=groupY[yCursor]
                yCursor+=1
            else:
                groupX[i]=groupX[nextPos]
                groupX[nextPos]=0
# doSortAndMerge(X,Y)  
# doSortCheck(X)
doImprovedSortAndMerge(X,Y)
doSortCheck(X)