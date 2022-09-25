
def solution():
    input_str = input().split()
    N,K = int(input_str[0]),int(input_str[1])
    input_score = input().split()
    scores = [int(x) for x in input_score]
    
    max_score = 0 
    # sort
    for i in range (0,K):
        max_score = scores[0]
        for j in range(0,len(scores)):
            if scores[j] > max_score:
                max_score = scores[j]
        scores.remove(max_score)

    print(max_score)
            
solution()