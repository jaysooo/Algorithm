# https://www.acmicpc.net/problem/10799

 # 1. 레이저 수
 # 2. 쇠막대 길
 # 3. 쇠막대 길이 내 레이저 수 +1 = 우리가 원하는 값
# 4. 막대의 길이는 중요하지 않다. 
# 5. 레이저가 인접해있는지는 중요하다.
# 6. 레이저가 인접해있지 않다면 괄호(여는/닫은) 갯수가 뎁스 가 될 것이다.
# 7. 레이저 바로 바깥 괄호부터는 쇠막대.
# 8. 쇠막대 개수부터 출력해보자

def getcnt(splitpipe):
    r=0
    # for c in splitpipe:
    #     if c=='L':
    #         r+=1
    r=splitpipe.count('L')
    return r+1


def solution(pipeline):
    parsed1=pipeline.replace('()','L')
    splitcnt=0
    pipe=''
    for e in parsed1:
        pipe+=e
        if e==')':
            i=pipe.rfind('(')
            pece=pipe[i:]       ##cnt
            splitcnt+=getcnt(pece)          
            pipe=pipe[:i]+pece[1:-1]
            

    print(splitcnt)


def main():
    #test_t='(((()(()()))(())()))(()())'
    test_t=input()
    #test_t='()(((()())(())()))(())'
    solution(test_t)


if __name__=='__main__':
    main()
