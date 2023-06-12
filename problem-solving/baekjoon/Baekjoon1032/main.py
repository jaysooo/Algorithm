

def solution():
    N = int(input())
    arr = []
    for i in range(0, N):
        input_str = input()
        arr += [input_str]

    end = len(arr[0])

    if len(arr) == 1:
        print(arr[0])
    else:
        start = 0
        output = ''
        while(start < end):
            ch = arr[0][start]

            for cmd in (arr[1:]):
                if ch != cmd[start]:
                    ch = '?'
                    break
            output += ch

            start += 1
        print(output)


if __name__ == '__main__':
    solution()
