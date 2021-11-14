
def set_test_case():
    N,L = input().split(" ")
    N,L = int(N),int(L)
    leak_pos = []
    leak_pos_org = input().split(" ")
    for v in leak_pos_org:
        leak_pos += [int(v)]

    return N,L,sorted(leak_pos)
         
def solution(N,L,leak_pos):
    cnt = 1 
    l = L
    
    start = 0 
    end = start+1

    while(end < N):
        if (leak_pos[end]-leak_pos[start]) >= L :
            cnt+=1
            start = end 
            end = start +1
        else:
            end+=1
        
    print(cnt)  

    

def main():
    N,L,leak_pos = set_test_case()
    solution(N,L,leak_pos)


if __name__=='__main__':
    main()