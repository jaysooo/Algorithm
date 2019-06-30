
# 5 100
# 3
# 4 100
# 3 100
# 7 100

# g 당 최저가를 찾아 Sort
# 최저가 g 부터 소유 금액을 차감 , 0이 될 떄까지. 
# 1000g 당 최저가를 출력하기 위해, 구매g 를 누적
# 1g 당 가격을 구하고 맵에 저장, K = 1g당 가격, V= 판매하는 g 수 
# map을 K 기준으로 정렬
# 계산.


trace=[]        #g당 가격

def search(_list,remain):
    if remain <= 0 or len(_list)==0:
        return 0
    p=remain/_list[0][1]
    if p > 0:
        remain-=_list[0][1]*p
        trace.append(_list[0][1])
    return search(_list[1:],remain)

def solution(_list):
    for i in range (0,len(_list)):
        print(search())

def main():
    stroed=[(5,100),(4,100),(3,100),(7,100)]
    solution(stroed)
    print(trace)

    
if __name__ == "__main__":
    main()
