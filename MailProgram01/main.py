#list=[-1, 3, -1, 5]
#list= [-5, -3, -1] 
list= [2, 4, -2, -3, 8]
maxVal=list[0]
result=[]    

def getSum(arrList):
    sum=0
    for i in arrList:
        sum=sum+i
    return sum
        
def getAnswer(start,end,arrList):
    global maxVal
    global result

    if maxVal <= getSum(arrList[start:end]):
        maxVal=getSum(arrList)
        result=arrList    

    if start<=end:
        return 0

    return getAnswer(start+1,end,arrList)+getAnswer(start,end-1,arrList)

getAnswer(0,len(list),list)
print(result)