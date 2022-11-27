import sys
input = sys.stdin.readline


def set_test_case():
    n = int(input())
    arr = []
    
    for i in range(0,n):
        input_str = input().split()
        arr += [[int(input_str[0]),int(input_str[1])] ]
    
    return arr
         
def solution():
    arr = set_test_case()
    end = len(arr)
    answer = []
    for i in range(0,end):
        count = 0 
        for j in range(0,end):
            if i == j:
                continue
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                count +=1

        answer += [str(count+1)]
    
    print(" ".join(answer))

solution()
        
        
        
                
            
            