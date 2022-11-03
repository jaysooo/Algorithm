

def solution():
    input_str = input().split()
    N,M = int(input_str[0]), int(input_str[1])
    A = []
    B = []
    AB = []
    for i in range(0,N):
        input_str = input().split()
        A += [[int(x) for x in input_str]]

    for i in range(0,N):
        input_str = input().split()
        B += [[int(x) for x in input_str]]
    
    
    for i in range(0,N):
        temp = []
        for j in range(0,M):
            temp += [A[i][j] + B[i][j]]
        AB += [temp]

    for i in AB:
        print(" ".join(list(map(lambda x : str(x),i))))
            

solution()

   
