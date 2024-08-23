

def solution():
    input_str = input().split(" ")
    triangle_candidate = sorted(list(map(int,input_str)))
    triangle_length = 0
    if triangle_candidate[2] >= (triangle_candidate[0]+triangle_candidate[1]):
        triangle_length = (triangle_candidate[0]+triangle_candidate[1]) *2 -1
    else:
        triangle_length = sum(triangle_candidate)



    print(triangle_length)

if __name__ == '__main__':
    solution()

