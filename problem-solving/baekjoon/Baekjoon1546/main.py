


def set_test_case():
    N = int(input())
    input_score = input().split()
    score = [int(x) for x in input_score]
    return score

    
def solution():
    scores = set_test_case()
    max_score = max(scores)
    sum = 0
    for score in scores:
        #print(f"score : {score}")
        new_score = score/max_score * 100
        sum += new_score

    print(sum/len(scores))

    
solution()
