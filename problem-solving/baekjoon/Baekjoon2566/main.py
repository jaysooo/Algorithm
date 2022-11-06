import sys

input = sys.stdin.readline
def solution():
    col,row = 0 , 0 
    max_col = 9 
    maxium_number = -1 
    for i in range(0,max_col):
        input_str = input().split()
        converted_input_str = [int(x) for x in input_str]
        tmp_maximum_number = max(converted_input_str)
        if maxium_number < tmp_maximum_number :
            maxium_number = tmp_maximum_number
            col = converted_input_str.index(tmp_maximum_number) +1
            row = i +1 
    
    print(maxium_number)
    print(f'{row} {col}')


solution()