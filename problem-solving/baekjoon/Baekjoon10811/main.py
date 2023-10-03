
import sys

input = sys.stdin.readline


def solution():
    input_str = input().split(" ")
    N, M = int(input_str[0]), int(input_str[1])
    bucket = [i for i in range(1, N+1)]
    for i in range(M):
        input_str = input().split(" ")
        i, j = int(input_str[0]), int(input_str[1])

        # for out of index Exception
        i -= 1
        j -= 1

        while(i < j):
            tmp = bucket[i]
            bucket[i] = bucket[j]
            bucket[j] = tmp
            i += 1
            j -= 1
        # print(f"current bucket = {bucket}")
    new_bucket = list(map(lambda x: str(x), bucket))
    # print(f"final bucket = {bucket}")
    print(" ".join(new_bucket))


if __name__ == '__main__':
    solution()
