
#inputStr="6 2 10 3"
inputStr=raw_input()

def solution(_input):
    split_elem= _input.split(" ")
    minA=0
    minB=0
    x=int(split_elem[0])
    y=int(split_elem[1])
    w=int(split_elem[2])
    h=int(split_elem[3])
    d1=w-x
    d2=h-y
 100
    if x<y:
        minA=x
    else:
        minA=y

    if d1<d2:
        minB=d1
    else:
        minB=d2
    

    if minA<minB:
        return minA
    else:
        return minB


print(solution(inputStr))