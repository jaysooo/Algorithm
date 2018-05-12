
nums=input()
str=input()

def isPrimeNumber(n):
    isPrime=True
    for i in range(2,n-1):
        if n%i==0:
            isPrime=False
            break
    
    return isPrime

def solution(_inputStr):
    numbers=_inputStr.split(" ")
    decimalCnt=0
    
    for v in numbers:
        num=int(v)

        if (num==1):
            continue
        elif (num==2):
            decimalCnt+=1
        else:
            if isPrimeNumber(num):
                decimalCnt+=1
            
            
    return decimalCnt

print(solution(str))