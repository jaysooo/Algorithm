

#inp="EGG FOO"
testStr="AAB FOO"

def solution(inputStr):
    splitStr=inputStr.split(" ")
    fromStr=splitString[0]
    toStr=splitString[1]

    encodeMap=dict()
    checkForStr=""
    isPossible=True
    for idx,s in enumerate(fromStr):
        if encodeMap.has_key(s):
           checkForStr+=encodeMap[s]
        else:
            encodeMap[s]=toStr[idx]
            checkForStr+=encodeMap[s]

        if checkForStr[idx]!=toStr[idx]:
            isPossible=False
            break
    
    return isPossible
        
        

print(solution(testStr))


