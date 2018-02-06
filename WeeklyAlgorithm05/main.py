
inputNum=3

#a = (  
#b = )
resultSet=set()

def solution(a,b,str,pattern):
    
    if (a < b) | (a > inputNum) | (b > inputNum):
        return 0

    str+=pattern

    if ((a==inputNum) & (b==inputNum)):
        
        resultSet.add(str)
        return 0
    
    
    
    return solution(a+1,b,str,'(')+solution(a,b+1,str,')')
    

result=''
solution(0,0,result,'')

print(resultSet)
