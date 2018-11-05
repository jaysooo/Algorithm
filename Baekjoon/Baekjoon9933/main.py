import collections

def main():
    passWord=dict()
    loopCnt=int(input())
    answer=""
    skip=False
    while loopCnt > 0:
        passStr=input()
        passWord[passStr]=True 
        if not skip:
                passStrReverse=passStr[::-1]
                if passStrReverse in passWord:
                        answer=passStr
                        skip=True
        loopCnt-=1


    print(len(answer),answer[int((len(answer)/2))])

if __name__ == "__main__":
        main()