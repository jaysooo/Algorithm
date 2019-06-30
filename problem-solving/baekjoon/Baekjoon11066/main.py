
# https://www.acmicpc.net/problem/11066
import copy

chapters=[40,30,30,50]
seqPool=set()

def call(list,idx):
    if idx<0 or idx+1 >= len(list):
        return 0
    numSet=(idx,idx+1)
    if numSet in seqPool:
        return 0
    
    seqPool.add(numSet)
    print('cur idx : %d ' % idx)

    return call(list,idx+1)+call(list,idx-1)

call(chapters,0)
print(seqPool)
