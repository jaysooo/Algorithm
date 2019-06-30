

inputStr=raw_input()
testT=inputStr.split(" ")

def solution(n1,n2):
    s=int(n2)
    r1=int(n1)
    return (2*s)-r1


print(solution(testT[0],testT[1]))