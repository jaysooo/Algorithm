

def calculate(A,B,N):
    R = 0

    while(A%B != 0 and N > 0 ):
        A = A * 10
        R = A//B
        R = int(str(R)[-1])
        A = A % B

        N = N-1

    return R

def solution():
    input_str = input().split(" ")
    result = calculate(int(input_str[0]),int(input_str[1]),int(input_str[2]),)
    print(result)


if __name__ == '__main__':
    solution()

