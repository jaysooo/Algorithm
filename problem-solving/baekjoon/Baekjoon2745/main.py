import math


def solution():
    input_str = input().split(" ")
    N = input_str[0]
    B = int(input_str[1])

    B_DIGIT = 0
    output = 0
    pos = 0

    for i in range(len(N)-1, -1, -1):
        if ord(N[i]) >= 65 and ord(N[i]) <= 90:
            B_DIGIT = ord(N[i]) - 55
        else:
            B_DIGIT = int(N[i])

        output += int(math.pow(B, pos)) * B_DIGIT
        pos += 1

    print(output)


if __name__ == '__main__':
    solution()
