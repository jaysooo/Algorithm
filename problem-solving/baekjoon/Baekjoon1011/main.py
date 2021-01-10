

def planetMove(start, end, jump, jumpchg, jumpcnt):

    # print('start : {}, end : {}, jump :{} jumpchg : {}'.format(
    #     start, end, jump, jumpchg))
    if start > end:
        return 0
    elif start == end and jump == 1:
        print('succed..')
        print('jump cnt : {} jump chg = {} jump= {}'.format(jumpcnt, jumpchg, jump))
        return 0
    else:
        start += jump  # next jump position
        jump += jumpchg  # next jump chg value
        jumpcnt += 1  # total jump count
    return planetMove(start, end, jump, jumpchg+1, jumpcnt)+planetMove(start, end, jump, jumpchg-1, jumpcnt)


def solution(start, end):
    planetMove(start, end, 0, 1, 0)


def main():
    solution(0, 3)
    # T = int(input())
    # for i in range(0, T):
    #     start, end = input().split(' ')


if __name__ == "__main__":
    main()
