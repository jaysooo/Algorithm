


def set_test_case():
    input_str = input().split()
    return input_str
    


def solution():
    AB = set_test_case()
    A = int(AB[0])
    B = int(AB[1])
    print(f"{A+B}")
    
solution()