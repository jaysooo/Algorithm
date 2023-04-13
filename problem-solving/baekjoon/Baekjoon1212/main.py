import math
def get_binary_digit(num):
    n = 0
    p = 0 

    while(num > 0):
        n += (num%2) * (10**p)
        p+=1
        num = num//2
    return n
    

def solution():
    N = input()
    output = []
    for idx, c in enumerate(N):
        n = get_binary_digit(int(c))
        if idx > 0 :
            output += str(n).rjust(3,'0')
        else:
            output += str(n)
            
    answer = "".join(output)
    print(answer)

            
        
    
solution()