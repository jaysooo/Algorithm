
def set_test_case():
    input_str = []
    for i in range(0,10):
        n = int(input())
        input_str += [n]
    return input_str
        

def solution():
    nums = set_test_case()
    result = set()
    for n in nums:
        result.add(n%42)
    
    print(len(result))

    
solution()