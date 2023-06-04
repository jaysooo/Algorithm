
from collections import deque


def loc_update(q, loc):
    if loc == 0:
        loc = len(q)-1
    else:
        loc -= 1
    return loc


def get_print_number(q, loc):
    cnt = 0

    while(len(q) > 0):
        out_priority = max(q)
        if loc == 0 and out_priority == q[loc]:
            cnt += 1
            break
        elif q[0] == out_priority:
            q.popleft()
            cnt += 1
            loc = loc_update(q, loc)
        else:
            q.rotate(-1)
            loc = loc_update(q, loc)
    return cnt


def solution():
    T = int(input())
    for i in range(0, T):
        input_str = input().split(" ")
        N, M = int(input_str[0]), int(input_str[1])
        DOCS = input().split(" ")
        print_queue = deque([int(x) for x in DOCS])
        result = get_print_number(print_queue, M)
        print(result)


if __name__ == '__main__':
    solution()
