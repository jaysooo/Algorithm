
def isValidWork(group,work):
    isValid=False
    for it in group:
        if ( it[0] < work[0] and it[1] <= work[0] and it[0] < work[1] and it[1] < work[1]):
            isValid=True
        elif ( it[0] > work[0] and it[1] > work[0] and it[0] >= work[1] and it[1] > work[1]):
            isValid=True
        else:
            isValid=False

    return isValid

def getMaxHour(workGroup):
    maxHour=len(workGroup[0])
    for i in workGroup:
        if maxHour< len(i):
            maxHour=len(i)
    return maxHour

def workAssignBuild(dailyWorks):
    workGroups=list()
    for it in dailyWorks:
        newGroup = [it]
        
        for w in workGroups:
            if isValidWork(w,it):
                w.append(it)
        workGroups.append(newGroup)

    rs=getMaxHour(workGroups)
    return rs

def solution():
    testT=int(input())

    for t in range (0,testT):
        dailyCase=int(input())
        dailyWorks=[]
        for c in range(0,dailyCase):
            work1=input().split(' ')
            work2=[int(elem) for elem in work1]
            dailyWorks.append(work2)

        output=workAssignBuild(dailyWorks)
        print(output)
        
        # dailyWorks.append(set(work))
        #print(dailyWorks)

solution()
