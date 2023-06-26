

def lcm(a, b):
    x = a
    y = b
    r = x

    while(r > 0):
        x = y
        y = r
        r = x % y
    return (a*b)//y


def solution():
    T = int(input())
    for i in range(0, T):
        input_str = input().split(' ')
     #   print(input_str)
        a = int(input_str[0])
        b = int(input_str[1])
        print(lcm(a, b))


if __name__ == '__main__':
    solution()
