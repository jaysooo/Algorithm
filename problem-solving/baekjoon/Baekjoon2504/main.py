import re
#testCase="([[[]]])"
testCase=raw_input()

#rule 1 = [X]
#rule 2 = (X)
#rule 3 = X+X
 
def convertX(x,rule):
      
    if rule==1:
        p=re.findall(r"\[\+(\d+)\]",x)
        r=int(p[0])*3
        return "+"+str(r)
    elif rule==2:
        p=re.findall(r"\(\+(\d+)\)",x)
        r=int(p[0])*2
        return "+"+str(r)    
    elif rule==3:
        p=re.findall(r"\+(\d+)",x)
        r=int(p[0])+int(p[1])       
        return "+"+str(r)     
    
def recursive(s):
    p=re.findall(r"\+\d+\+\d+",s)
    if len(p)>0:
        for item in p:
            v=convertX(item,3)
            s=s.replace(item,v)
        return recursive(s)

    if (s.find("(")==-1) and (s.find("[")==-1):
        return str(s)[1:]
    
    p=re.findall(r"\[\+\d+\]",s)
    if len(p)>0:
        for item in p:
            v=convertX(item,1)
            s=s.replace(item,v)
        return recursive(s)
    
    p=re.findall(r"\(\+\d+\)",s)
    if len(p)>0:
        for item in p:
            v=convertX(item,2)
            s=s.replace(item,v)  
        return recursive(s)
    
    return 0
    
def solution(_in):
    s=_in.replace("()","+2")
    s=s.replace("[]","+3")
    rs=recursive(s)
    print(rs)
    
    
solution(testCase)
            
class SimpleStack(object):
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,item):
        self.top+=1
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        item=self.stack[self.top]
        self.stack.remove(item)
        self.top-=1
        return item
    
    def isEmpty(self):
        return True if self.top==-1 else False
        
def solution2(testCatse):
    s=SimpleStack()
    bracketRule={}
    bracketRule[']']='['
    bracketRule[')']='('
    isMatching=True
    
    #testCase Input
    for i in range(0,len(testCase)):
        print(s.stack)
        if not (testCase[i] in bracketRule):
            s.push(testCase[i])
        else:
            item = s.pop()
            if (bracketRule[testCase[i]]!=item):
                isMatching=False
               
                break
    
                
    return isMatching        

