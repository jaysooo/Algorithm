

testNum=8
#testNum = int(input())
def solution(n):
    
    tmp=str(n)
    cnt=0

    while(True):
        
         #sum
        if len(tmp)==1:
            tmp='0'+str(n)
            
        sum = int(tmp[0])+int(tmp[-1])
        #newNum
        newNum=tmp[-1]+str(sum%10)

        #add cnt
        cnt+=1
        tmp=newNum
        if int(newNum)==n:
            break




    return cnt



print(solution(testNum))
    
    
