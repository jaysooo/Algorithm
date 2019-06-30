
def pizzaSet(s,m,l,p):
    if (s+m+l)>p:
        return 0
    elif(s+m+l)==p:
        return 1
    else:
        return pizzaSet(s+s,m,l,p)+pizzaSet(s,m+m,l,p)+pizzaSet(s,m,l+l,p)

def main():
    output=[]
    inputT=int(input())
    for i in range(0,inputT):
        tcase=input().split(' ')
        s,m,l,p=[int(elem) for elem in tcase]
        res=pizzaSet(s,m,l,p)
        if res>0:
            output.append(1)
        else:
            output.append(0)

    for r in output:
        print(r)

if __name__=='__main__':
    main()