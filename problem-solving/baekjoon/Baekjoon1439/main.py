import sys

input = sys.stdin.readline().rstrip


def main():
    S = input()
    zero = S.split('1')
    one = S.split('0')
    filter_zero = list(filter(lambda x: x != '', zero))
    filter_one = list(filter(lambda x: x != '', one))
    print(min([len(filter_zero), len(filter_one)]))


if __name__ == '__main__':
    main()
