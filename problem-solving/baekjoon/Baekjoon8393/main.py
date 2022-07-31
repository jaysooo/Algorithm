
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

    

def solution():
    N = int(input())
    sum  = 0
    for i in range(1,N+1):
        sum+=i
    print(sum)


solution()
    