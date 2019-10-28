def rev(n):
    digits=[]
    d=0
    while(n>0):
        digits.append(n%10)
        n=int(n/10)
        d+=1
    rev=0
    for i in digits:
        rev+=pow(10,d-1)*i
        d-=1

    return rev

def main():
    n1,n2=input().split(' ')
    print(rev(rev(int(n1))+rev(int(n2))))

if  __name__=="__main__":
    main()