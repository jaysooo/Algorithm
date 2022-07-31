import sys
input = sys.stdin.readline

def solution():
    N = int(input().rstrip())
    for i in range(0,N):
        input_str = input().rstrip().split()
        print(f"{(int(input_str[0]))+ (int(input_str[1]))}")


solution()