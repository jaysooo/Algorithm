
#inputT= [-5,-3,1]

inputT= [-5,3,1]
def insertionSort(_arr,_idx):
    
    for i in range(1,len(_arr)):
        tmp=_arr[i]
        aux= i-1
        while (aux>=0) and (_arr[aux]<tmp ):
            _arr[aux+1]=_arr[aux]
            aux-=1
        
        _arr[aux+1]=tmp

    print(_arr)


def solution(_arr,idx):
    
    maxSet=[]
    maxVal=_arr[0]
    cnt=0
    for i in _arr:
        if maxVal < i :
            maxVal=i

    maxSet.append(maxVal)
    cnt=1

    if cnt==idx:
        return maxVal
    else:
        while(cnt<idx):
            maxVal=_arr[0]
            for i in _arr:
                if maxSet[-1] > i and maxVal < i:
                    maxVal=i

            cnt+=1
            maxSet.append(maxVal)

    
    print(maxSet[-1])
    return maxSet[-1]
    
            

solution(inputT,3)