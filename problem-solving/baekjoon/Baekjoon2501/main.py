

def solution():
    input_str = input().split()
    N, K = int(input_str[0]), int(input_str[1])

    divisor=[]
    i = 1
    while i <= N:
        if N % i ==0:
            divisor.append(i)
        i+=1
    if (K-1) >= len(divisor):
        print(0)
    else:
        print(divisor[K-1])


if __name__=="__main__":
    solution()