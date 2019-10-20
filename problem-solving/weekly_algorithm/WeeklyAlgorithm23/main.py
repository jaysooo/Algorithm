# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
# 정수 배열이 주어졌을 때, 짝수 위치의 원소가 양 옆의 원소보다 큰 수가 되도록 배치하시오.

# 배열에는 중복 원소가 없다고 가정합니다.

 

# Input: [1, 2, 3, 4, 5, 6, 7]

# Output: [1, 3, 2, 5, 4, 7, 6]




# Input: [9, 6, 8, 3, 7]

# Output: [6, 9, 3, 8, 7]

 

# Input: [6, 9, 2, 5, 1, 4]

# Output: [6, 9, 2, 5, 1, 4]

def arraySwap(arr,srcIdx,dstIdx):
    tmp=arr[dstIdx]
    arr[dstIdx]=arr[srcIdx]
    arr[srcIdx]=tmp
    return arr

def reArrange(targetArr):
    cur=1
    limit=len(targetArr)
    while(cur<limit):
        #case ) last element comparison
        if cur==limit-1 :           
            if targetArr[cur] < targetArr[cur-1]:
                arraySwap(targetArr,cur,cur-1)       
        elif targetArr[cur] < targetArr[cur-1] or targetArr[cur] < targetArr[cur+1]:
            if targetArr[cur-1]> targetArr[cur+1]:
                arraySwap(targetArr,cur,cur-1)  
            else:
                arraySwap(targetArr,cur,cur+1)  
        cur=cur+2
    return targetArr

def main():
    T=[1, 2, 3, 4, 5, 6, 7]
    answer=reArrange(T)
    print(answer)




if __name__ == "__main__":
    main()


 