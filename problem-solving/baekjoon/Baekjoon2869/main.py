import math
def solution():
    input_str = input().split()
    A = int(input_str[0])
    B = int(input_str[1])
    V = int(input_str[2])

    x = (V-B)/(A-B)
    print(math.ceil(x))
    

solution()