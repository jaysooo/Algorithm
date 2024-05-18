
def solution():
	
    N = int(input())
    S = 1
    square = 3
    while(N > 1 and S<N):

        square = (square * 2) -1
        S += 1

    if N == 0:
        print(4)
    elif N == 1:
        print(9)
    else:
        print(square*square)


if __name__=="__main__":
    solution()