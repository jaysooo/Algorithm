# input: [3, 4, 5, 1, 2], 4
# output: 1
# input: [2, 4, 5, 1], 3
# output: -1
# input: [4, 6, 7, 8, 1, 2, 3], 6
# output: -1

testCase=[4, 6, 7, 8, 1, 2, 3]
def solution(arr,k):
    cursor=0
    posDir=1
    kPosition=-1
    
    if (arr[0] < k):
        cursor=0
    else:
        cursor=len(arr)-1
        posDir=-1
    
    while(cursor >= 0 and cursor < len(arr)):
        if posDir == 0 and arr[cursor] < k:
            break
        elif posDir == 1 and arr[cursor] > k:
            break
            
        if arr[cursor]==k:
            kPosition=cursor
            break
        cursor=cursor+posDir
    return kPosition

print(solution(testCase,5))
    

        

    
        
    
