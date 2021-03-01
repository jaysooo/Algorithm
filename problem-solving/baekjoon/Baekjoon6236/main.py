def binarySearch(databucket,searchValue):
    startPos=0
    endPos=len(databucket)-1
    mid=(endPos+startPos)//2

    while(startPos<endPos):

        if databucket[mid]== searchValue:
            return mid
        elif databucket[mid] < searchValue:
            startPos=mid
        else:
            endPos=mid
        mid=(endPos+startPos)//2


#K 값으로 M 개의 파티션을 나눌수 있는지 확인
def withdrawCountCheck(databucket,minWithdraw):
    count=1
    sum=0
    for i in databucket:
        sum+=i
        if sum>minWithdraw:
            count+=1
            sum=i
        
    return count

        

def inputTest():
    N,M=input().split(" ")
    N=int(N)
    M=int(M)
    testCaseList = []
    for i in range(0,N):
        testCaseList.append(int(input()))
    
    return N,M,testCaseList


def solution():
    # sample
  #  N=7
 #   M=5
   # bucket = [100,400,300,100,500,101,400] # MoneyUsePlan
    N,M,bucket=inputTest()

    maxWithdraw = 100000
    minWithdraw = 0
    midWithdraw=0

    while(True):
        midWithdraw = (minWithdraw+maxWithdraw)//2
        cnt= withdrawCountCheck(bucket,midWithdraw)
        if cnt == M :
            break
        if cnt < M:
            maxWithdraw=midWithdraw
        else:
            minWithdraw=midWithdraw

    print(midWithdraw)
        

solution()
