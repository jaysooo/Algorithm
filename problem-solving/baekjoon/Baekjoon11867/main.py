def solution():
    x,y=input().split(' ')
    x=int(x)
    y=int(y)

    if x%2!=0 and y%2!=0:
        print('B')
    else:
        print('A')


solution()