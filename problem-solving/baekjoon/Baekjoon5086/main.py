
def solution():

    while(True):
        input_str = input().split(" ")
        a = int(input_str[0])
        b = int(input_str[1])

        if a == 0 and b == 0:
            break

        elif b % a == 0 :
            print('factor')
        elif a % b == 0:
            print('multiple')
        else:
            print('neither')


if __name__ == '__main__':
    solution()
