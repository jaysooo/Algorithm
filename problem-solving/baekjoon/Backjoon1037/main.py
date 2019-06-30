
N=int(input())
#arr=raw_input().split(" ")
for i in range(0, N):
    arr=int(input())

if len(arr)!=N:
    exit(1)

if len(arr)==1:
    print(arr[0])
else:
    arr.sort()
    print(int(arr[-1])*int(arr[0]))

