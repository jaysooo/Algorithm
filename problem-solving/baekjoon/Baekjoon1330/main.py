
def solution():
    input_str = input().split()
    A,B = int(input_str[0]),int(input_str[1])
    comparison = '=='
    if A < B:
        comparison = '<'
    elif A > B : 
        comparison = '>'
    else:
        pass
    print(comparison)
        
solution()