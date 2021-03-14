def myDFS(N,M,caseMap):
    stack = []
    visited = []
    success = False
    for i in range (0,N):
        visited.append([False for i in range(M)])

    #set start pos
    for i in range(0,M):
        stack.append((0,i))

    while(len(stack) >0):
        loc = stack.pop()
        row = loc[0]
        col = loc[1]

        #out of index case
        if row < 0 or col < 0 or row >= N or col >= M or visited[row][col]:
            continue

        visited[row][col]=True

        #Block case
        if caseMap[row][col] == 1:
            continue

        print("current row : {} col : {}  val : {}".format(row,col,caseMap[row][col]))

        stack.append((row,col-1))
        stack.append((row,col+1))
        stack.append((row-1,col))
        stack.append((row+1,col))
        
        #reach to Out line 
        if (row+1) == N:
            success = True

    return success

def inputCase():
    NM= input().split(" ")
    N,M=int(NM[0]),int(NM[1])
    caseMap = []
    for i in range (0,N):
        inline = input()
        flatten = [int(x) for x in inline]
        caseMap.append(flatten)
    return N,M,caseMap

def solution():
    N,M,caseMap = inputCase()
    rs=myDFS(N,M,caseMap)
    if rs ==True:
        print("YES")
    else:
        print("NO")
    #print(caseMap)    



solution()