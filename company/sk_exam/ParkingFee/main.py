#inputStr="10:00 13:21"
inputStr="10:00 10:00"
testSet=set()

testSet.add("11")
testSet.add("22")
testSet.add("22")

print(testSet)

defaultFee=2
firstHour=3 
remainningHour=4

def solution(_str):
    parsedStr=_str.split(" ")        
    parkStartStr=parsedStr[0]
    parkEndStr=parsedStr[1]

    startHour=int(parkStartStr[0:2])
    endHour=int(parkEndStr[0:2])

    startMinute=int(parkStartStr[3:])
    endMinute=int(parkEndStr[3:])

    minusHour=endHour-startHour
    minusMin=endMinute-startMinute   

    if minusHour < 1:
        return defaultFee+firstHour
    elif (minusHour==1) and minusMin > 0:
        return defaultFee+firstHour+remainningHour
    elif (minusHour>1) and minusMin == 0:
        return defaultFee+firstHour+(remainningHour*(minusHour-1))
    else:
        return defaultFee+firstHour+(remainningHour*(minusHour))

print(solution(inputStr))