

def comparison2(aList,bList):
    res='D'
    aList=sorted(aList)
    bList=sorted(bList)
    cursor=0
    while(cursor<len(aList) and cursor< len(bList)):
        if aList[cursor]>bList[cursor]:
            res='A'
        elif aList[cursor]<bList[cursor]:
            res='B'
        
        cursor+=1
    
    if res=='D' and len(aList)>len(bList):
        res='A'
    elif res=='D' and len(aList)<len(bList):
        res='B'

    return res
    

def comparison(aDic,bDic):
    res='D'
    iter=sorted(list(set().union(aDic.keys(),bDic.keys())))

    for i in iter:
        if i not in aDic:
            res='B'
        elif i not in bDic:
            res='A' 
        elif aDic[i]>bDic[i]:
            res='A'
            break
        elif aDic[i]<bDic[i]:
            res='B'
            break

    return res
def buildDic(bucket):
    dic={}
    for e in bucket:
        if e in dic:
            dic[e]=dic[e]+1
        else:
            dic[e]=1
    return dic

def main():
    inputT=int(input())
    output=[]
    for i in range(0,inputT):
        sisIn=input().split(' ')
        friIn=input().split(' ')
        
        # aDic=buildDic(sisIn[1:])
        # bDic=buildDic(friIn[1:])
        # res=comparison(aDic,bDic)
        res=comparison2(sisIn[1:],friIn[1:])
        output.append(res)
    for r in output:
        print(r)
        
        

if __name__=='__main__':
    main()