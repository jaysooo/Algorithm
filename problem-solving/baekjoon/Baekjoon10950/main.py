

def solution():
    N = int(input())
    for i in range(0,N):
        input_str = input().split()
        output = (lambda x : int(x[0])+ int(x[1]))(input_str)
        print(output)


solution()
    