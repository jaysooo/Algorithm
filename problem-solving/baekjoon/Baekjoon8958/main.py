
def parse_score(answer):
    sum = 0 
    end = len(answer)
    offset = 0 
    score = 0 
    
    while(offset < end):
        if answer[offset] == 'O':
            score +=1
            sum += score
        else:
            score = 0 
        
        offset +=1

    return sum
            
        

def solution():
    N = int(input())
    
    for i in range(0,N):
        answer = input()
        print(parse_score(answer))

        


solution()