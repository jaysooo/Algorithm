def solution():
    N = input()
    input_str = input().split()
    list_n = [int(x) for x in input_str]
    print(f"{min(list_n)} {max(list_n)}")


solution()
    