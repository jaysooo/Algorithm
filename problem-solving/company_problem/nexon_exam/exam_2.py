import copy
#testCase=[0,1,0,0,0,1,0,1]
testCase=[0,0,1,1,1,0,0]

def swap(arr,a,b):
    tmp=arr[a] 
    arr[a]=arr[b]
    arr[b]=tmp
    return arr

def sortByPivot(arr,pivotVal):
    shiftCnt=0
    for i in range(1,len(arr)):
        j=i
        while(j>0):
            if arr[j]!=arr[j-1] and arr[j-1]==pivotVal :
                arr=swap(arr,j,j-1)
                shiftCnt+=1
            j-=1
    
    print(arr)
    return shiftCnt

def solution(arr):

    arr2=copy.deepcopy(arr)
    v1=sortByPivot(arr,0)
    v2=sortByPivot(arr,1)

    return v1 if v1 < v2 else v2


print(solution(testCase))


