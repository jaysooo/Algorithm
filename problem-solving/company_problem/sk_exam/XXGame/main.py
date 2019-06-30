t=[[1, 2], [2, 3]]

def calCostByHeight(land,P,Q):
    minCost=calCost(land,P,Q,1)
    for i in range(1,4):
        cost = calCost(land,P,Q,i)
        if minCost > cost:
            minCost=cost

    return minCost


def calCost(partedLand,P,Q,H):
    cost=0
    for i in partedLand:
        for j in i:
            diff=j-H
            cost+= diff*Q if diff > 0 else (abs(diff)*P)
    return cost

def solution(land, P, Q):
    answer = -1

    answer=calCostByHeight(land,P,Q)
    return answer


print(solution(t,3,2))
