def solution(arr):
    answer = True

    arr.sort()
    j=arr[0]
    for i in range(0,len(arr)):
        if arr[i]!=j:
            answer=False
            break
        j+=1


    return answer
    
print(solution(t))