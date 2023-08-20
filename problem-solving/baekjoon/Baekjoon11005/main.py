
def solution():
    # N = 60466175
    # B = 36
    input_str = input().split(" ")
    N = int(input_str[0])
    B = int(input_str[1])
    output = ''

    while(N >= 1):
        a = N % B
        N = N//B
        if a >= 10:
            a = chr(a + 55)

        output = str(a) + output

    print(output)


if __name__ == '__main__':
    solution()
