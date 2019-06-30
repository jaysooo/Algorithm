
N=int(input())
#total=1
attandSet=set()
#charSet=set()
#for i in range(0,N): 
#    total*=3

#2L , 3 continuos A
def isNotAttandance(att):
    lcnt=0
    acnt=0

    for i in range(0,len(att)-2):
        if att[i:i+3]=='AAA':
            return True

    for i in att:
        if i =='L':
            lcnt+=1
        if lcnt>=2:
            return True

    return False


def solution(att):
    
    if isNotAttandance(att):
        return 0

    if len(att)==N:
        #if isNotAttandance(att):
         #   attandSet.add(att)
        return 1

    return solution(att+'O')+solution(att+'L')+solution(att+'A')

solution('')
#print(attandSet)
print(solution(''))
#print( (total-len(attandSet))%1000000 )