
maxMove=0

def moveKangaroo(a,b,c,move):
    global maxMove
    if (c-b)<=1 and (b-a)<=1:
        if maxMove < move:
            maxMove=move
        return 0
    else:
        return moveKangaroo(b,c-1,c,move+1)+moveKangaroo(a,a+1,b,move+1)

def solution(pos):
    a,b,c=pos
    moveKangaroo(a,b,c,0)

def main():
    pos=[int(x) for x in input().split(" ")]
#    pos=[3,5,9]
    solution(pos)
    print(maxMove)

if __name__ =="__main__":
    main()