import collections

# def run():
#     monsterByName= collections.OrderedDict()
#     monsterByName['null']=0
#     cnt,answer=input().split(' ')
#     calledMonster=[]
#     for i in range(1,int(cnt)+1):
#         name=input()
#         monsterByName[name]=str(i)

#     for i in range(0,int(answer)):
#         monster=input()
#         calledMonster.append(monster)

#     for seq in calledMonster:
#         if ord(seq[0]) > 47 and ord(seq[0]) < 58:
#             print(list(monsterByName.keys())[int(seq)])
#         else:
#             print(monsterByName[seq])

# def main():
#     run()


def solution():
    testCase=input().split(' ')
    monsterDictByName={}
    monsterDictByNumber=[]
    N=int(testCase[0])
    M=int(testCase[1])
    monsterDictByNumber.append(' ')

    for i in range(100000):
        monsterDictByName[i] = None

    for i in range(1,N+1):
        nm=input()
        monsterDictByNumber.append(nm)
        idx=nm[0:10]
        if idx in monsterDictByName:
            monsterDictByName[idx][nm]=i
        else:
            newSet={}
            newSet[nm]=i
            monsterDictByName[idx]=newSet
    
        # monsterDict[str(i)]=nm
        # monsterDict[nm]=str(i)
    for i in range(0,M):
        aw=input()
        idx=aw[0]
        if ord(idx)>=48 and ord(idx)<=57:
            idx=int(aw)
            print(monsterDictByNumber[idx])
        else:
            idx=aw[0:10]
            print(monsterDictByName[idx][aw])
        
    
    #print(monsterDict)






def main():
    solution()

if __name__ =="__main__":
    main()