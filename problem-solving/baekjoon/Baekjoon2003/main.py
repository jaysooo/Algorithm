N, M = 0, 0


def set_test_case():
    global N, M
    input_str = input().split(" ")
    N, M = int(input_str[0]), int(input_str[1])
    input_str = input().split(" ")
    arr = [int(x) for x in input_str]
    return arr


def solution():
    global N, M
    arr = set_test_case()
    cnt = 0
    end = len(arr)
    prefix_sum = [0] * (end)
    prefix_sum[0] = arr[0]
    for i in range(1, end):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    for i in range(0, end):
        if prefix_sum[i] == M:
            cnt += 1
        for j in range(0, i):
            if prefix_sum[i] - prefix_sum[j] == M:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    solution()
