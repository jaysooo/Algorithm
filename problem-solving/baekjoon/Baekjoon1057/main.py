

def set_test_case():
    input_str= input()
    parse_str = input_str.split(" ")
    N, A, B  = int(parse_str[0]),int(parse_str[1]),int(parse_str[2])
    return N,A,B    
    
def divide(num):
    if num == 1:
        return num
    elif num % 2 != 0:
        return num//2 + 1
    else:
        return num//2

def solution():
    N,A,B = set_test_case()
    round_count = 0
    while(True):
        round_count +=1 
        A = divide(A)
        B = divide(B)
        if A == B :
            break
    print(round_count)

def main():
    solution()
    
if __name__ == '__main__':
    main()
