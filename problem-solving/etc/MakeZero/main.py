
#1 = '+'
#2 = '-'
#3 = 'combine'
list=[1,'+',2,' ',3,'-',4]

for i in list:
    if i =='+':
    print(i)

exit(1)
final_rs=set([])
def opr(list,op,rs):
    if len(list)==1:
        if list[0]==0:
            #final_rs.add(set((i) for i in rs))
            print(rs)
        return -1

    tmp=[len(list)-1]
 
    if op==1:       
        tmp[0]=list[0]+list[1]
        rs.append('+')
    elif op==2:
        tmp[0]=list[0]-list[1]
        rs.append('-')
    elif op==3:
        tmp[0]=int(`list[0]`+`list[1]`)
        rs.append(' ')

    rs.append(list[1])
    tmp+=list[2:]
    opr(tmp,1,rs)
    opr(tmp,2,rs)
    opr(tmp,3,rs)

def getAnser(list):
    rs=[list[0]]
    opr(list,1,rs)
    opr(list,2,rs)
    opr(list,3,rs)

list=[1,2,3]
#list=[1,2,3,4,5,6,7]
getAnser(list)
print(final_rs)