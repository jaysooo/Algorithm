import math
def is_ichin(source):
    result = True
    offset = 1
    while(offset<len(source)):
        if source[offset] == '1' and source[offset-1] == '1':
            result=False
            break
        offset +=1
        
    return result
            
ichin_array = [0,1,1,2]

def get_ichin(n):
    if n < len(ichin_array):
        return ichin_array[n]
    else:
        ichin = get_ichin(n-1)+get_ichin(n-2)
        ichin_array.append(ichin)
        return ichin
    
def solution_1():
    N = int(input())
    S = int(math.pow(2,N))
    cnt = 0 
    for num in range(0,S):
        s = bin(num)[2:]
        if len(s) == N and is_ichin(s):
            cnt+=1
        #print(f"num : {num}\t binary : {s} ichin : {is_ichin(s)}")
    
    print(cnt)
    
    
def solution():
    N = int(input())
    print(get_ichin(N))
    
#solution_1()
solution()