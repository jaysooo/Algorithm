


def solution(_list,IdxList,x):
    if x>=len(_list)-1:
        print(IdxList)
        return 0
    if x>-2:
        IdxList.append(x)
    return solution(_list,IdxList,x+2)+solution(_list,IdxList,x+3)

def main():
    t_list=[ 6, 10, 13, 9, 8, 1 ]
    idxList=[]
    solution(t_list,idxList,-2)



if __name__=="__main__":
    main()
