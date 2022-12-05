import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N = int(input())
    if N == 1:
        print(1)
        return 
    queue = deque([int(x) for x in range(1,N+1)])
    queue.popleft()
    while(len(queue) > 1 ):
        queue.append(queue.popleft())
        queue.popleft()
        
    
    print(queue[0])
    


solution()