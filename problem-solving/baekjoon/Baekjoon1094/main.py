stick=64
x=int(input())
stickList=[64,32,16,8,4,2,1]

def solution(list,x):

    cnt=0
    sum=0
    for i in list:
        if i==x:
            cnt=1
            break
        elif (i+sum) == x:
            cnt+=1
            break
        elif (i+sum) < x:
            sum+=i
            cnt+=1  
    return cnt

print(solution(stickList,x))
     
        
            
            
            
            
