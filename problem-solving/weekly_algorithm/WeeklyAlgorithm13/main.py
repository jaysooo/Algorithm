
Input=['apple', 'apps', 'ape']

def solution(_arr):
    idx=0

    while(True):
        
        for i in range(1,len(_arr)):
            str1=_arr[i]
            str2=_arr[i-1]

            if len(str1)<=idx or len(str2)<=idx:
                return idx
            elif str1[idx]!=str2[idx]:
                return idx
            else:
                if i==len(_arr)-1:
                    idx+=1
    
    return idx
    #print(idx)

print(solution(Input))
