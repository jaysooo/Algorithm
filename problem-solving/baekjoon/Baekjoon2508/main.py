# .>o<
# v.^.
# ooo.
# ^.^.
# 


# >v<
# >o<
# >^<

def solution(r,c):
    #variable init
    r=int(r)
    c=int(c)
    candy_loc=[]
    candy_cnt=0
    candy_bucket=[[0 for i in range(c)] for j in range(r)]

    for i in range(0,r):
        in_str=input()
        for c,v in enumerate(in_str):
            candy_bucket[i][c]=v


    #-> candy check
    for i in range(0,r):
        for j in range(0,c-1):
            if candy_bucket[i][j:j+3]==['>','o','<']:
                print(candy_bucket[i][j:j+3])
                candy_loc.append([i,j+1])
                candy_cnt+=1

    for i in range(0,c):
        for j in range(0,r-1):
            if candy_bucket[i][j] =='v' and candy_bucket[i+1][j]=='o' and candy_bucket[i+2][j]=='^':
                dup=False
                for k in candy_loc:
                    if k[0]==i+1 and k[1]==j:
                        dup=True
                if dup is not True:
                    candy_cnt+=1


    print(candy_cnt)



def main():
    T=int(input())
    input()
    for i in range (0,T):
        r,c=input().split(' ')
        solution(r,c)

main()