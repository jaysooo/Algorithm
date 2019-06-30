import collections

def run():
    monsterByName= collections.OrderedDict()
    monsterByName['null']=0
    cnt,answer=input().split(' ')
    calledMonster=[]
    for i in range(1,int(cnt)+1):
        name=input()
        monsterByName[name]=str(i)

    for i in range(0,int(answer)):
        monster=input()
        calledMonster.append(monster)

    for seq in calledMonster:
        if ord(seq[0]) > 47 and ord(seq[0]) < 58:
            print(list(monsterByName.keys())[int(seq)])
        else:
            print(monsterByName[seq])

def main():
    run()

if __name__ =="__main__":
    main()