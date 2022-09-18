

def set_test_case():
    N = int(input())
    score_of_student = []
    for i in range(0,N):
        input_str = input().split()
        input_score = input_str[1:]
        scores = [int(x) for x in input_score]
        score_of_student+=[scores]
        
    return score_of_student


def solution():
    scroe_of_student = set_test_case()
    for group in scroe_of_student:
        avg = sum(group)/len(group)
        more_than_avg = list(filter(lambda a: a > avg,group))

        more_than_group = len(more_than_avg)
        rate = more_than_group/len(group)* 100 
        more_than_group = len(more_than_avg)
        print("{:.3f}%".format(rate))

        


solution()

# 2
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
