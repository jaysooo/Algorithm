# test case
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

# class mystack
# func main()
#   - input testcase 
#   - solution func call

# main idea
#   - ( 열린 괄호는 stack 에 put
#   - ) 닫힌 괄호는 stck pop 
#   - 테스트 케이스 문자열의 처리 끝에 stack 의 크기에 따라 Yes/No 출력
# 짝이 안맞거나  -> No
# 마지막에 스택에 아이템이 있을떄. -> No

class MyStack:
    buff=[]
    def __init__(self):
        self.items=0
    #put
    def push(self,item):
        self.buff.append(item)
        self.items+=1
    #pop
    def pop(self):
        if self.isEmpty():
            return 'null'
        item=self.buff.pop()
        self.items-=1
        return item

    def __size__(self):
        return self.items

    def isEmpty(self):
        if self.items > 0:
            return False
        else:
            return True

def solution(t_str):
    mst=MyStack()   
    flag=True
    for c in t_str:
        if c==')':
            item=mst.pop()
            if item=='null':
                flag=False
        else:
            mst.push(c)

    if flag is False or mst.items>0:
        print("NO")
    else:
        print("YES")

def main():
    incaseNum=input()
    for t in range(0,int(incaseNum)):
        c_str=input()
        solution(c_str)

if __name__=="__main__":
    main()