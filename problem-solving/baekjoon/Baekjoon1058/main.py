

def friByFri(fraList):
    
    for c in fraList:


def solution():
    fra_num=int(input())
    fra_list=[]
    for i in range(0,fra_num):
        fra_list+=[[c for c in input()]]

    max_fra_cnt=0
    for i,ifra in enumerate(fra_list):
        fra_cnt1=0
        fra_cnt2=0

        for j in ifra:
            if j=='Y':
                fra_cnt1+=1

        if max_fra_cnt<=fra_cnt1:
            max_fra_cnt=fra_cnt1
        fra_cnt1=0
            

        for j in range(0,i):
            if fra_list[i][j]=='Y':
                fra_cnt1+=1
            if fra_list[j][i]=='Y':
                fra_cnt2+=1
                #print('fra_list[{}][{}] = {}'.format(i,j,fra_list[i][j]))
        
        if fra_cnt1==fra_cnt2:
            if max_fra_cnt<=fra_cnt1:
                max_fra_cnt=fra_cnt1
    print(max_fra_cnt)
        
        

             



solution()