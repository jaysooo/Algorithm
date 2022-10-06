import sys

input = sys.stdin.readline

count_recursive = 0 
count_loop = 0 
def fib(n):
    global count_recursive
    if n <= 2:
        count_recursive+=1
        return 1
    
    return fib(n-1) + fib(n-2)

def fibonacci(n):
    global count_loop
    arr = [0]*400
    arr[1] = 1
    arr[2] = 1

    if n <=2 :
        return arr[n]
    for i in range (3,n+1) :
        
        count_loop+=1
        arr[i] = arr[i-1] + arr[i-2]
        
    return arr[n]

    
def solution():
    n = int(input())
    fib(n)
    fibonacci(n)

    print(f"{count_recursive} {count_loop}")

solution()