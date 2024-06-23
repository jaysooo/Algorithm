from collections import deque
# 5
# 3 2 1 -3 -1
def set_test_case():
    T = int(input())
    S = input().split(" ")
    data = []
    idx = 1
    for i in S:
        data.append([idx,int(i)])
        idx += 1 

    q = deque(data)
    return q

def solution():
    q = set_test_case()
    output = []
    while len(q) > 0:
        pops_element = q.popleft()
        output.append(pops_element[0])
        if pops_element[1] > 0 :
            next_rotate = (pops_element[1] * -1) +1
        else:
            next_rotate = pops_element[1] * -1

        q.rotate(next_rotate)
    output = list(map(lambda x: str(x),output))

    print(" ".join(output))

if __name__=="__main__":
    solution()
