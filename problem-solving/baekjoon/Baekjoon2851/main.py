
def solution():
    input_score=[]
    score=0
    pre_diff=0
    diff =0 

    for i in range(0,10):   
        s=int(input())
        input_score.append(s)

        diff=100-score
        if score>=100:                              
            if abs(pre_diff) < abs(diff):
                score=100-pre_diff
            break
     
    print(score)


def main():
    solution()

if __name__=='__main__':
    main()
