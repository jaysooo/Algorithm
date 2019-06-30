stepHeight=7
k=3

# def solution(_stepHeight,_k):
#     stepCnt=0
#     for step in range(1,_stepHeight+1):
#         if (stepCnt+step)!=_k:
#             stepCnt+=step

#     return stepCnt
def recursiveStepCnt(curStep,cnt,k):
    
    cnt+=curStep
    if cnt == k:
        return 0
    elif curStep==stepHeight:
        return cnt
    else:
        recursiveStepCnt(curStep+1,cnt,k)


def solution(stepHeight,k):

    





print(solution(stepHeight,k))