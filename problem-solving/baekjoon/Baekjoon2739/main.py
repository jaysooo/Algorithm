
def solution():
    N = int(input())
    gugudan = [(x,x * N) for x in range(1,10)]
    for p in map(lambda x: f"{N} * {x[0]} = {x[1]}",gugudan):
        print(p)


solution()