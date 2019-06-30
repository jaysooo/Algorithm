

#N 을 입력 받는다.
#N 수 만큼 O, L, A를 추가하여 재귀호출을 한다.
#출석일 경우 1을 리턴하도록 한다.

#개근상을 받을 수 있는 경우만 리턴한다.


N=100
#2L , 3 continuos A
def isNotAttandance(att):

    for i in range(0,len(att)-2):
        if att[i:i+3]=='AAA':
            return True
    if len([x for x in att if x == 'L'])>=2:
        return True
    return False


def solution(att):
    
    if isNotAttandance(att):
        return 0
    if len(att)==N:
        return 1
    return solution(att+'O')+solution(att+'L')+solution(att+'A')


def solution2(N):
    total=4

    for x in range(0,N):
        total*=x


result=solution('')
print(result)
#print( (total-len(attandSet))%1000000 )
