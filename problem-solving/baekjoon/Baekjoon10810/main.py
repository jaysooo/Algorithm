

def solution():
    input_str = input().split(" ")
    N, M = int(input_str[0]), int(input_str[1])
    bucket = [0] * N

    for i in range(M):
        input_str = input().split(" ")
        command = [int(n) for n in input_str]
        i, j, k = command[0], command[1], command[2]
        bucket[(i-1):(j)] = [k] * (j-i + 1)
        # print(bucket)
    print(" ".join(map(str, bucket)))


if __name__ == '__main__':
    solution()
