from fractions import Fraction

def GCD(N,M):
    while(M!=0):
        tmp=N%M
        N=M
        M=tmp

    return N
        
def solution():
    in_case=input().split(' ')
    a=int(in_case[0])   
    b=int(in_case[1])   
    #a=4
    #b=3

    print(b-GCD(a,b))

solution()
#print(GCD(3,7))