
def getLpn(pattern):
    lpn=[0]
  #  print(len(pattern))
    cursor=0
    for i in range(1,len(pattern)):
        if pattern[cursor]==pattern[i]:
                print('same:',pattern[i])
                tmp=lpn[i-1]
                lpn.append(tmp+1)
                cursor+=1
        else:
            lpn.append(0)
            cursor=0
    #print(lpn)
    return lpn

def getIndex(str,pattern):
    i=0
    j=0
    L=len(targetStr)
    N=len(pattern)
    while i<L:
        if targetStr[i]==pattern[j]:
            i+=1
            j+=1
            if j==N:
                return i-N
                #print('find str index : ',i-N)
                break
        elif j>0:
            
            j=lpn[j-1]
        else:
            i+=1

    return -1


targetStr="aaabbcd"
pattern="ab"

lpn=getLpn(pattern)
print(getIndex(targetStr,pattern))
