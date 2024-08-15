import sys
input=sys.stdin.readline
from collections import OrderedDict

def get_avg(arr):
    return int(round(sum(arr)/len(arr),0))

def get_median_value(arr):
    return sorted(arr)[int(len(arr)//2)]

def get_mode_value(arr):
    map = OrderedDict()
    for i in sorted(arr):
        if i not in map:
            map[i] = 1
        else:
            map[i] +=1
    max_freq = max(map.values())
    max_freq_arr = [k for k, v in map.items() if v == max_freq]
    return max_freq_arr[1] if len(max_freq_arr) > 1 else max_freq_arr[0]

def get_max_range(arr):
    if len(arr) == 1:
        return 0
    elif max(arr) > 0 and min(arr) < 0 :
        return abs(max(arr) + abs(min(arr)))
    elif max(arr) <0 and min(arr) <0 :
        return abs(min(arr)) - abs(max(arr))
    else:
        return max(arr) - min(arr)



def set_test_case():
    n = int(input())
    arr = []
    for i in range(0,n):
        arr += [int(input())]

    return arr

def solution():
    arr = set_test_case()
 #   arr = [1,3,8,-2,2]
#    arr=[4000]
#    arr = [-1,-2,-3,-1,-2]
    # arr = [0,0,-1]
    print(get_avg(arr))
    print(get_median_value(arr))
    print(get_mode_value(arr))
    print(get_max_range(arr))
    # print(arr)



if __name__ == '__main__':
    solution()