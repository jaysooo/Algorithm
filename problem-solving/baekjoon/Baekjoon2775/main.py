
def get_people_of_room(k_flow,n_room):
    #k_flow = 3
    #n_room = 4
    people_of_room = [x for x in range(1,n_room+1)]
    
    for f in range(1,k_flow+1):
        current_flow = []
        for i in range(1,len(people_of_room)+1):
            current_flow += [sum(people_of_room[:i])]
        
        people_of_room = current_flow
    return people_of_room[n_room-1]

    
def solution():
    N = int(input())
    for i in range(0,N):
        k = int(input())
        n = int(input())
        print(get_people_of_room(k,n))
        
solution()