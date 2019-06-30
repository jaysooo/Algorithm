#inputStr="1 8 3 2"
inputStr="3 0 7 0"

def getMaxPosition(_arr,maxNum):
    tmpMax=0
    tmpIdx=0
    for idx,val in enumerate(_arr):
        if val >= tmpMax and val <=maxNum:
            tmpMax=val
            tmpIdx=idx

    return tmpIdx
    # order
    # 0 <= H1 <=2  , 0<= H2 <=4,   0<= M1 <=5,     0<= M2 <= 9
    # if H1 = 1, 0<= H1 <=9, 0<= M1 <=5,     0<= M2 <= 9
    #Exception , 24:00, 24:59, 23:59, if 24, only 00

def solution(_inputStr):
    parsedStr=_inputStr.split(" ")
    digits=[int (x) for x in parsedStr]
    limitDigits=[2,4,5,9]
    time=""
    
    for li in limitDigits:
        timePos=getMaxPosition(digits,li)
        time+=str(digits[timePos])
        digits.remove(digits[timePos])

        if time=="24":
            limitDigits=limitDigits[0:2]+[0,0]
        elif time=="1" or time=="0":
            limitDigits=limitDigits[0:1]+[9,5,9]
            

    time=time[:2]+":"+time[2:]
    if len(digits)>0:
        time="Not Possible"
    
    print(time)
        

    

solution(inputStr)
    
