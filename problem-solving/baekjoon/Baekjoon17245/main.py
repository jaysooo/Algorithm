TOTAL_COMPUTERS=0
MIN_COMPUTERS=0
MAX_COMPUTERS=0

def getMinMinute(servers):
    global TOTAL_COMPUTERS, MIN_COMPUTERS,MAX_COMPUTERS
    start=0
    end=MAX_COMPUTERS

    while(start<end):
        mid=(start+end)//2
        sumOfComputer=0

        for i in servers:
            if i>mid:
               sumOfComputer+=mid
            else:
                sumOfComputer+=i
        #if sumOfComputer==MIN_COMPUTERS:
         #   start=end
        if sumOfComputer<MIN_COMPUTERS:
            start=mid+1
        else:
            end=mid
        
    return end
    

def solution():
    global TOTAL_COMPUTERS,MIN_COMPUTERS,MAX_COMPUTERS
    arr=[]
    N=int(input())
    for i in range (0,N):
        in_line=input().split(' ')
        tmp=[int(x) for x in in_line]
        if max(tmp)>=MAX_COMPUTERS:
            MAX_COMPUTERS=max(tmp)
        TOTAL_COMPUTERS+=sum(tmp)
        arr+=tmp


    if TOTAL_COMPUTERS%2==0:
        MIN_COMPUTERS= (TOTAL_COMPUTERS//2)
    else:
        MIN_COMPUTERS= (TOTAL_COMPUTERS//2)+1
    print(getMinMinute(arr))

if __name__=='__main__':
    solution()
