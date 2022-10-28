import sys

input = sys.stdin.readline

def get_accumulate_numbers(arr):
    new_arr = [0] * len(arr)
    for idx, va in enumerate(arr):
        if idx == 0 :
            new_arr[idx] = va
        else:
            new_arr[idx] = new_arr[idx-1] + va
    
    return new_arr
        

def solution():
    input_str = input().split()
    N , M = int(input_str[0]),int(input_str[1])
    numbers = input().split()
    numbers = [int(x) for x  in numbers]
    accumulate_numbers = get_accumulate_numbers(numbers)

    for i in range(0,M):
        input_range = input().split()
        i, j = int(input_range[0]),int(input_range[1])
        if i > 1:
            print(accumulate_numbers[j-1]- accumulate_numbers[i-2])
        else:
            print(accumulate_numbers[j-1])
    
solution()