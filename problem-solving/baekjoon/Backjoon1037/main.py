
def set_test_case():
    N = int(input())
    factors = input().split(" ")
    factors = sorted([int(x) for x in factors])
    return factors
    
def solution():
    T = set_test_case()
    result = T[0] * T[-1]
    print(result)
    
solution()

    