


def solution():
    while(True):
        input_str = input().split()
        A , B = int(input_str[0]) , int(input_str[1])
        if A ==0 and B == 0:
            break
        else:
            print(f"{A+B}")
        

solution()
