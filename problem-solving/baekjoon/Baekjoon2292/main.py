

def solution():
#    N = 1000000000
    N = int(input())
    cnt = 1
    iter = 1
    while iter < N:
        iter = (cnt * 6) + iter
        cnt += 1

    print(cnt)




if __name__ == '__main__':
    solution()