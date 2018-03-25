inputT = [[2,4],[1,5],[7,9]]

def solution(T):
    
    size=len(T)
    i,j=0
    while(i<size):
        
        for j in range(i+1,len(T),1):
            arr1=T[i]
            arr2=T[j]

            #비교군이 포함된 경우
            if ((arr1[0]>=arr2[0]) && (arr1[1]<=arr2[1])):
                inputT[i]=inputT[j]
                

            
            #비교군이 겹치는 경우

            #비교군이 다른경우
    

    for idx,elem in enumerate(T):
        print(idx,elem)

solution(inputT)