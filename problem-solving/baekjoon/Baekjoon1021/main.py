from collections import deque

def set_test_case():
    in_line = input().split(" ")
    n,m = int(in_line[0]),int(in_line[1])

    in_line = input().split(" ")
    pop_list = [int(x) for x in in_line]

    return n,m,pop_list

def pop_simulate(q,v):
    dir= 1 if q.index(v) > len(q)//2 else - 1
    turn=0

    while(True):
        if q[0] == v:
            q.popleft()
            break
            
        else:
            q.rotate(dir)
            turn += 1
    return turn

def solution():
    n,m,pop_list = set_test_case()
    turns = []
    q = deque([i for i in range(1,n+1)])

    #q.rotate(1) # to right
    
    for v in pop_list:
        result = pop_simulate(q,v)
        turns +=[result]
    print(sum(turns))


if __name__=="__main__":
    solution()
