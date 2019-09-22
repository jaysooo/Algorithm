
import copy

# In)
# 3
# 3 4 5
# 1 0 1 0
# (+) (-) (*) (/)
# Out)
# 35
# 17

# 모든 경우의 수식을 스트링을 만든다.

# 수식을 계산한다.
# 최대값과 최소값을 찾는다.
mathStore = set()
caseNum=6
opStore=[2,1,1,1]

progression=['1', '2', '3', '4', '5' ,'6']

def mathBuild(cur_ops,cur_math,tg_op,idx):
    cur_math+=progression[idx]
    if idx==caseNum-1:
        mathStore.add(cur_math)
    idx=idx+1
    if cur_ops[tg_op] >= opStore[tg_op]:
        return 0
    
    if tg_op==0 and opStore[tg_op] > 0:
        cur_math+='+'
        cur_ops[tg_op]=cur_ops[tg_op]+1      
    elif tg_op==1 and opStore[tg_op] > 0:
        cur_math+='-'
        cur_ops[tg_op]=cur_ops[tg_op]+1  
    elif tg_op==2 and opStore[tg_op] > 0:
        cur_math+='*'
        cur_ops[tg_op]=cur_ops[tg_op]+1 
    elif tg_op==3 and opStore[tg_op] > 0:
        cur_math+='/'
        cur_ops[tg_op]=cur_ops[tg_op]+1   
    else:
        if idx==caseNum-1:
            mathStore.add(cur_math)
        return 0

    return mathBuild(progression,cur_ops,cur_math,0,idx)+mathBuild(progression,cur_ops,cur_math,1,idx)+mathBuild(progression,cur_ops,cur_math,2,idx)+mathBuild(progression,cur_ops,cur_math,3,idx)
    
def build(progression):
    cur_ops=[0,0,0,0]
    mathBuild(progression,cur_ops,'',0,0)
    cur_ops=[0,0,0,0]
    mathBuild(progression,cur_ops,'',1,0)
    cur_ops=[0,0,0,0]
    mathBuild(progression,cur_ops,'',2,0)
    cur_ops=[0,0,0,0]
    mathBuild(progression,cur_ops,'',3,0)

def main():
#    caseNum=input()
    
    build(progression)
    print(mathStore)
       
def f(n):
    if n<=1:
        return 1
    
    return n*f(n-1)

if __name__=='__main__':
    print(f(3))
    # calc=process('1-2/3+4+5*6')
 #   print(calc)