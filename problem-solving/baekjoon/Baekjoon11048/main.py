

maxCandyCnt=0
N=4
M=3

def inputdata():
    N,M=int(input().split(' '))
    cmap=[]
    for i in range(0,N):
        list=[input().split(' ')]
        cmap[i]=list
    
def travelMap(_cmap,curPos,candycnt):
    global maxCandyCnt
    x,y=curPos
    if x < 0 or y < 0 or x >= N or y >=M:
        return
    elif (x+1)==N and (y+1)==M:
        candycnt+=_cmap[x][y]
        if maxCandyCnt <= candycnt:
            maxCandyCnt=candycnt
        return
    else:
        candycnt+=_cmap[x][y]
        travelMap(_cmap,[x,y+1],candycnt)
        travelMap(_cmap,[x+1,y],candycnt)
        travelMap(_cmap,[x+1,y+1],candycnt)
    

def solution(cmap):
    travelMap(cmap,[0,0],0)
    print("max = ",maxCandyCnt)

def main():
    #cmap=[[1,0,0],[0, 1, 0],[0, 0 ,1]]  
    #cmap=[[1,2, 3, 4],[0, 0, 0, 5],[9, 8, 7, 6]]     
    cmap=[[1, 2, 3],[6, 5, 4],[7, 8, 9],[12, 11, 10]]
    solution(cmap)



if __name__=="__main__":
    main()
    #inputdata()