testT="abcbb"

def solution(str):
    subStrCnt=0
    maxSubStrCnt=0
    charStore=dict()
    startIdx=0
    for obj in str:
        
        if charStore.has_key(obj):
            charStore=dict()
            charStore[obj]=True
            if subStrCnt>=maxSubStrCnt:
                maxSubStrCnt=subStrCnt
            subStrCnt=1
            loopIdx=startIdx
            while(loopIdx>0):
                loopIdx-=1
                if testT[startIdx]==testT[loopIdx]:
                    loopIdx=0
                else:
                    charStore[testT[loopIdx]]=True
                    subStrCnt+=1
        else:
            charStore[obj]=True
            subStrCnt+=1
    
        startIdx+=1

    if subStrCnt>=maxSubStrCnt:
            maxSubStrCnt=subStrCnt
    return maxSubStrCnt
    
print(solution(testT))