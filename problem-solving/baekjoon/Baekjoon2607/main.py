

def comparison(t1,t2):
    cnt=0
    for c in t1:
        if len(t2)>0:
            try:
                idx=t2.index(c)
                if idx >= 0:
                    t2 = t2[:idx] + t2[idx+1:]
                    cnt+=1
            except Exception as e:
                None

    return cnt


def solution(words):
    similar_cnt=0
    t=words[0]  
   
    d=len(t)        # 타겟 문자열 길이
    for s in words[1:]:
        c=len(s)   
        if d == c:     
            r=comparison(t,s)       
            if r==d or (r+1)==d:        #하나가 부족한 경우 , 변경하는 경우
                similar_cnt+=1
                
        elif d == (c+1):    
            r=comparison(t,s)
            if (r+1)==d:             # 하나를 더하는 경우
                similar_cnt+=1
                
        elif d == (c-1):
            r=comparison(t,s)
            if r==(d):        #하나를 뺴는 경우
                similar_cnt+=1
            
    print(similar_cnt)


                
        
        
def main():
    words=[]
    T=int(input())
    for i in range(0,T):
        words.append(input())
    # words=['DOG','GO']
    solution(words)


if __name__=='__main__':
    main()
