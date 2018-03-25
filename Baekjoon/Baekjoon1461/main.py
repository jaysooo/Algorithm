#comInput=raw_input()
#bookPosition=raw_input()

#comands=comInput.split(" ")
#bookList=[int(x) for x in bookPosition.split(' ')]

#N=int(comands[0])
#M=int(comands[1])
N=7 
M=2
bookList=[-37,2,-6 ,-39, -29,11,-28]

bookList.sort()
#print(bookList)


def getSteps(rangeList):
    print("rangeList: ",rangeList)
    rangeList.sort()
    steps=0
    for i in range (0,len(rangeList)):
        if i == 0:
            continue
        
        stpes=rangeList[i]-rangeList[i-1]
    
    
        
   
    return steps


def solution(list):
    lastBook=[]
    step=0
    #print(list)
    if abs(list[0]) > abs(list[-1]):
        lastBook=list[0:M]
        list=list[M:]
    else:
        lastBook=list[:-1*M]
        list=list[:-1*M]
        
    while len(list)>0:
        print(list)
        print(step)
        if abs(list[0]) > abs(list[-1]):
            step+=getSteps(list[0:M])
           # print("cut: ",list[0:M])
            #step+=abs(list[0])*2
            list=list[M:]
        else:
            step+=getSteps(list[-M:])
           # print("cut :",list[-M:])
            #step+=abs(list[-1])*2
            list=list[:-1*M]

    if abs(lastBook[0])>abs(lastBook[1]):
        step+=abs(lastBook[0])
    else:
        step+=abs(lastBook[1])
    print(lastBook)         
    print(step) 

solution(bookList)