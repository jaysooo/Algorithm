

def my_max(a, b):
    return a if a >= b else b


def solution():
    #stairs = [10, 20, 15, 25, 10, 20]
    N = int(input())
    stairs = [0] * N
    dp = [0] * len(stairs)
    for i in range(0, N):
        stairs[i] = int(input())

    if N >= 3:

        dp[0] = stairs[0]
        dp[1] = my_max(stairs[0]+stairs[1], stairs[1])
        dp[2] = my_max(stairs[0]+stairs[2], stairs[1]+stairs[2])

        for i in range(3, len(stairs)):
            dp[i] = my_max(dp[i-2]+stairs[i],
                           dp[i-3]+stairs[i-1]+stairs[i])
        print(dp[-1])
    else:
        print(sum(stairs))


if __name__ == '__main__':
    solution()
