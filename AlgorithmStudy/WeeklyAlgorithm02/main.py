def ffibonacci(n):
    sum=0
    a1=0
    a2=1
    a3=0
    while(a3<n):
        a3=a1+a2
        a1=a2
        a2=a3
        if a3%2==0:
            sum+=a3

    return sum


rs = ffibonacci(12)
print(rs)

