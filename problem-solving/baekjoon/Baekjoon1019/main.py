

def extract_digit_from_number(arr, num):

    while num > 0:
        arr[num % 10] += 1
        num = num//10
    return arr


def solution():
    n = 1
    while(True):
        if n == 0:
            break
        n = int(input())
        digit_arr = [0] * 10  # output = [0,1,2,3,4,5..,9]

        for i in range(1, n+1):
            extract_digit_from_number(digit_arr, i)

        output = ' '.join([str(x) for x in digit_arr])
        print(output)


# 10
# 1 2 1 1 1 1 1 1 1 1

# 19
# 1 12 2 2 2 2 2 2 2 2

# 100
# 11 21 20 20 20 20 20 20 20 20

# 199
# 29 140 40 40 40 40 40 40 40 40

# 1000
# 192 301 300 300 300 300 300 300 300 300

# 10000
# 2893 4001 4000 4000 4000 4000 4000 4000 4000 4000

if __name__ == '__main__':
    solution()
