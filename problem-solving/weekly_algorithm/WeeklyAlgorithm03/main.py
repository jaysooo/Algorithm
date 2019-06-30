import sys

def getAnser(n,a):
    if n<a:
        return getAnser(n+1,a)+getAnser(n+2,a)+getAnser(n+3,a)
    elif n==a:
        return 1
    else:
        return 0

def main():
    testC=[]
    for arg in sys.argv[2:]:
        testC.append(arg)
    
    for t in testC:
        #print(getAnser(0,t))
        print(t)
        
    print('==answer==')
    print(getAnser(0,4))
    print(getAnser(0,7))
    print(getAnser(0,10))


if __name__ == "__main__":
    main()

