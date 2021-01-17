

def solution():
    #inputCase=input().split(' ')
    seq = 1

    while(True):
        inputCase = input().split(' ')
        L = int(inputCase[0])
        P = int(inputCase[1])
        V = int(inputCase[2])
        if L == 0 and P == 0 and V == 0:
            break
        div = V//P
        mod = V % P
        if L < mod:
            out = div*L+L
        else:
            out = div * L + mod

        print("Case {}: {}".format(seq, out))
        seq += 1


if __name__ == '__main__':
    solution()
