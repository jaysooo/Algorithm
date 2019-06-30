
caseNum=int(input())
print(caseNum)
testCase=[]
for i in range(0,caseNum):
    testCase.append(int(input()))

#testCase=[3,4,5,6,7]
#ex)
#1 = 1
#2+1 = 3
#3+2+1 = 6
#4+3+2+1 = 10
#=180

def solution2(testT):
    for idx,val in enumerate(testT):
        if idx==0:
            continue
        
        print(idx*val)
        
def solution(testT):
    first=False
    for i in range(1,len(testT)):
        temp=0
        for j in range(i,-1,-1):
            temp=temp+(i-j)

        if (first==False):
            cost=temp
            first=True
        else:    
            cost=temp*cost

    cost=cost%1000000007
    print(cost)



solution(testCase)