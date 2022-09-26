
def solution():
    N = int(input())
    i = 666
    while(True):
        if str(i) == '666' or str(i).find('666') >=0:
            N -=1
        
        if N == 0:
            print(i)
            break
            
        i+=1 

solution()