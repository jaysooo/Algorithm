import datetime
N=10
Ti=[]
Pi=[]
allCase=[]



# def getCase(caseList,idx,cur=[]):
#     if idx>=len(caseList):
#         if len(cur)>0:
#             allCase.append(list(cur))
#         return

#     cost=idx+Ti[idx]



def getCost(caseList):
    cost=0
    if len(caseList)>1:
        cur=1
        while(cur<len(caseList)):
            if (caseList[cur-1]+Ti[caseList[cur-1]]<=Ti[caseList[cur]]):
            cur+=1



    for i in caseList:
        cost+=Pi[i]
    return cost

def solution():
    # Ti=[3,5,1,1,2,4,2]
    # Pi=[10,20,10,20,15,40,200]
    # Ti=[1,1,1,1,1,1,1,1,1,1]
    # Pi=[1,2,3,4,5,6,7,8,9,10]
    Ti=[5,4,3,2,1,1,2,3,4,5]
    Pi=[50,40,30,20,10,10,20,30,40,50]
    maxCost=0
    

# solution()

allCase=[]
def gen(arr,idx=0,cur=[]):
    if idx >= len(arr):
        if len(cur)>0:
            allCase.append(list(cur))
        return
            
    gen(arr,idx+1,cur)
    inclue=list(cur)
    inclue.append(arr[idx])
    gen(arr,idx+1,inclue)

def getAllCase(arr):
    global allCase
    gen(arr)

caseArray = [x for x in range(0,N)]
getAllCase(caseArray)


#ref  
#https://stackoverflow.com/questions/53106794/algorithm-for-all-subsets-of-array