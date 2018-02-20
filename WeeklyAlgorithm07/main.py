import numpy as np

input=[2,5,6,1,10]
target=8
result=set()

def solution(arr,idx1,idx2):
    
    if (arr[idx1]+arr[idx2])==target:
        result.add(idx1)
        result.add(idx2)
        return 1
    
    if idx1>=idx2:
        return 0

    return solution(arr,idx1+1,idx2)+solution(arr,idx1,idx2-1)

solution(input,0,len(input)-1)

print(result)
    

