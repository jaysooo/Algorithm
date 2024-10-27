
def solution():
    n = int(input().strip())
    for i in range(n):
        a ,b  = map(int,input().split(" "))
        x = a
        number_rules = []
        number_rules += [x%10]
        for i in range(10):
            x = x * a
            x = x % 10
            number_rules += [x%10]

        distinct_rules = []
        for v in number_rules:
            if v not in distinct_rules:
                distinct_rules.append(v)

        idx = b % len(distinct_rules) -1

        if distinct_rules[idx] == 0:
            answer = 10
        else:
            answer = distinct_rules[idx]
        print(answer)



if __name__ == '__main__':
    solution()