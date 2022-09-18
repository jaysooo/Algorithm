

def solution():
    input_str = input().split()
    x = int(input_str[1])
    input_n = input().split()
    output_n = [i for i in input_n if int(i) < x]
    print(" ".join(output_n))


solution()