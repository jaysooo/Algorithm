
import sys
input = sys.stdin.readline


def solution():
    input_str = input().split(" ")
    n, s = int(input_str[0]), int(input_str[1])
    input_str = input().split(" ")
    arr = [int(x) for x in input_str]
    prefix_sum = [0] * (n+1)

    # two pointer
    sp = 0
    ep = 1
    min_cnt = n
    while(ep <= n):
        prefix_sum[ep] = prefix_sum[ep-1] + arr[ep-1]
        ep += 1
    ep = 0

    if prefix_sum[-1] < s:
        print(0)
        return 0

    while(sp <= ep and ep <= n):
        if (prefix_sum[ep] - prefix_sum[sp]) >= s:
            if min_cnt > (ep-sp):
                min_cnt = (ep-sp)
            sp += 1
        else:
            ep += 1

    print(min_cnt)


if __name__ == '__main__':
    solution()
