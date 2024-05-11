def get_coins(total_cost:int = 0):
    rule = [25,10,5,1]
    output = []
    total_cost = total_cost * 100

    for r in rule:
        if (total_cost / r) >= 1:
            count = total_cost // (r*100)
            output.append(str(count))
            total_cost -= count * (r * 100)
        else:
            output.append(str(0))
    return " ".join(output)


def solution():
    N = int(input())
    for i in range(N):
        T = int(input())
        print(get_coins(T))

if __name__ == '__main__':
    solution()