

def solution():
    input_str = input().split(" ")
    N, M = int(input_str[0]), int(input_str[1])
    min_set_price, min_price = 1000, 1000
    result = 0
    for i in range(0, M):
        input_str = input().split(" ")
        set_price, price = int(input_str[0]), int(input_str[1])
        if set_price > price * 6:
            set_price = price*6
        min_set_price = set_price if set_price < min_set_price else min_set_price
        min_price = price if price < min_price else min_price

    if N >= 6:
        set_count = N//6
        remainder = N - (set_count) * 6
        result = set_count * min_set_price
        if remainder * min_price > min_set_price:
            result += min_set_price
        else:
            result += remainder * min_price

    else:
        if min_price > min_set_price:
            min_price = min_set_price
        result = N * min_price

    print(result)


if __name__ == '__main__':
    solution()
