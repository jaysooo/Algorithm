# https://www.acmicpc.net/problem/1120



def strCompare(a,b):
    i=0
    diff=0
    while(i<len(a)):
        if a[i]!=b[i]:
            diff+=1
        i+=1
    return diff


def solution(inputTestCase):
    a,b=inputTestCase
    mindiff=len(b)
    #print('a = %s , b = %s ' % (a,b))
    for i in range(0,(len(b)-len(a))+1):
        diff=strCompare(a,b[i:])
        if mindiff>diff:
            mindiff=diff
        #print('diff = %d ' % diff)


    print(mindiff)


def main():
    T=input().split(' ')
    solution(T)


if __name__=='__main__':
    main()