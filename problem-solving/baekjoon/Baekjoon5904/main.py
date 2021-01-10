import math


def build_locs(size):
    mid_locs=[3]
    new_locs=[]
    i=0
    while i < size:
        new_locs=mid_locs+[mid_locs[int(len(mid_locs)/2)]+1]+mid_locs 
        mid_locs=new_locs
        i+=1

    return new_locs
#    print(new_locs)

def solution(N):
    m_locs=[1]
    std=1
    size=int(math.sqrt(N))
    inc_locs=build_locs(size)

    for v  in inc_locs:
        m_locs+=[std+v]
        std=std+v
    print(m_locs)
    
    #print(m_locs)
    if N in m_locs:
        return "m"
    else:
        return "o"


def main():
    N=int(input())
    print(solution(N))
main()
