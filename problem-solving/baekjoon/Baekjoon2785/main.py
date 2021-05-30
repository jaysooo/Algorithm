

def getMinimumChainRing(chains,v_chains):
    endRingPos = chains-1
    startRingPos = 0
    while(True):
        if  startRingPos == endRingPos:
            print(chains - 1 - endRingPos)
#            print("minimum chain Ring count : {} ".format(endRingPos-1))
            break
        elif v_chains[startRingPos]==0:
            startRingPos+=1
        else:
            v_chains[startRingPos]-=1
            endRingPos-=1



def solution():
    chains = int(input())
    org_v_chains = input().split(" ")
    #chains = 5
    #org_v_chains=[1,1,1,2]
   # org_v_chains=[4,3,5,7,9]
    v_chains = [int(x) for x in org_v_chains]
    getMinimumChainRing(chains,sorted(v_chains))


if __name__=="__main__":
    solution()