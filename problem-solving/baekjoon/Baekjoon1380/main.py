def get_name(arr):
    name = ''
    for idx, name in enumerate(arr):
        if name is not 'retrived':
            return idx


def solution():
    names = []
    info = []
    output = []
    seq = 1
    while(True):
        input_str = input().split(" ")
        if input_str[0] == '0':
            name = names[get_name(info)]
            output += [f"{seq} {name}"]
            seq += 1
            break
        elif len(input_str) == 1:
            if len(info) > 0:
                name = names[get_name(info)]
                output += [f"{seq} {name}"]
                seq += 1
            n = int(input_str[0])
            info = [''] * n
            names = []
            for i in range(n):
                name = input()
                names += [name]
        else:
            number = int(input_str[0])
            tag = input_str[1]

            if info[number-1] == '':
                info[number-1] = tag
            else:
                info[number-1] = 'retrived'

    print("\n".join(output))


if __name__ == '__main__':
    solution()
