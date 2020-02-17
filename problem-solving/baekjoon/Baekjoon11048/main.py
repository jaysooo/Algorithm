import sys
import random
sys.setrecursionlimit(100000)

maxCandyCnt=0
N=500
M=500
isFirst=True
cmap=[]
call_pos=dict()
call_cnt=0

def inputdata():
    global cmap,N,M

    in_first=input().split(' ')
    N=int(in_first[0])
    M=int(in_first[1])
#    cmap=[]
    cmap=[0 for i in range(0,N)]
    for i in range(0,N):
        in_val=input()
        map_val=in_val.split(' ')
        cmap[i]=map_val

    #print(cmap)
    
def travelMap(curPos,candycnt,travelPath):
    global maxCandyCnt,isFirst,call_pos,cmap,call_cnt
    call_cnt+=1
    x,y=curPos

    if x < 0 or y < 0 or x >= (M) or y >= (N):
        return
    elif (x)==(M-1) and (y)==(N-1):
        if travelPath in call_pos.keys():
            return
        else:
            call_pos[travelPath]=True
            #print(travelPath)
        candycnt+=int(cmap[x][y])
        if isFirst:
            maxCandyCnt=candycnt
            isFirst=False

        if maxCandyCnt <= candycnt:
            maxCandyCnt=candycnt
        #print('current_candy {}'.format(candycnt))
        return
    else:
  
        travelPath+=str(x)+str(y)
        candycnt+=int(cmap[x][y])
        travelMap([x,y+1],candycnt,travelPath)
        travelMap([x+1,y],candycnt,travelPath)
        travelMap([x+1,y+1],candycnt,travelPath)

def solution(cmap):
    travelMap([0,0],0,'')
#    print("max = ",maxCandyCnt)
    print(maxCandyCnt)

def main():
    global cmap
    #cmap=[[1,0,0],[0, 1, 0],[0, 0 ,1]]  
    #cmap=[[1, 2, 3, 4],[0, 0, 0, 5],[9, 8, 7, 6]]     
    #cmap=[[1, 2, 3],[6, 5, 4],[7, 8, 9],[12, 11, 10]]
#    inputdata()
    cmap=[[random.randint(0,10) for i in range(0,100)] for i in range(0,100)]

    solution(cmap)




if __name__=="__main__":
    main()
    print(call_cnt)
#print(call_pos)