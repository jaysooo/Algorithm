

def solution():
    input_case = input().split(" ")
    Et, St, Mt = int(input_case[0]), int(input_case[1]), int(input_case[2])
    # Et, St, Mt = 15, 28, 19
    E, S, M, = 0, 0, 0
    YEAR = 0
    while(True):
        E += 1
        S += 1
        M += 1
        YEAR += 1
        if (E == Et and S == St and M == Mt):
            break

        E = E % 15
        S = S % 28
        M = M % 19

    print(YEAR)


if __name__ == '__main__':
    solution()
