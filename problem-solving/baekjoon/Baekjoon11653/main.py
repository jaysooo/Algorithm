def get_small_number(number):
    is_small_number=[]

    if number == 1 :
        is_small_number = [1]
    else:
        for i in range(2,number+1):
            if number % i == 0:
                is_small_number +=[i]    
    
    return is_small_number
     


def solution():
    N = int(input())
    arr = get_small_number(N)
    small_number = arr.pop(0)
    while(N>1):
        if N % small_number == 0 :
            N = N//small_number
            print(small_number)
        else:
            if len(arr) == 0 :
                print(small_number)
                break
            small_number = arr.pop(0)

        
solution()