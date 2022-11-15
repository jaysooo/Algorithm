
import math
import sys
input = sys.stdin.readline


def solution():
    while(True):
        input_str = input()
        if input_str.rstrip() == '0 0 0':
            break
        triangle = sorted([int(x) for x in input_str.split()])
        
        if math.pow(triangle[2],2) == math.pow(triangle[1],2)+math.pow(triangle[0],2):
            print('right')
        else:
            print('wrong')


solution()
        
