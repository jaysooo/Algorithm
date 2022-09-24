

def set_test_case():
    N = int(input())
    bucket = []
    for i in range(0,N):
        bucket += [int(input())]

    return bucket
        
    
def solution():
    bucket = set_test_case()
    #bucket = [5,4,3,2,1]

    # insertion sort 
    for i in range(1,len(bucket)):
        temp = bucket[i]
        for j in range(i,-1,-1):
            if bucket[j] > temp:
                bucket[j+1] = bucket[j]
                bucket[j] = temp
    
    for i in bucket:
        print(i)
    
            
            
                
                
                

solution()
