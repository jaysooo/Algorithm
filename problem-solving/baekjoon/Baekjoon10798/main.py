

def assignStr(source,dest,vlevel):
    for c in source:
        dest[vlevel]=c
        vlevel+=5

    return dest
        

def main():
    dest=[None]*(5*15)

    for i in range(0,5):
        bucket=input()
        assignStr(bucket,dest,i)        
    
    result=''
  
    for s in dest:
        if s is not None:
            result+=s
    print(result)
        
if __name__=="__main__":
    main()
