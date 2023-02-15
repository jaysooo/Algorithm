import math
def solution():
    while(True):
        input_str = input()
        if input_str == '0':
            break
        mid = math.ceil(len(input_str)/2)
        stack = []
        if (len(input_str)%2 != 0):
            stack += input_str[:mid-1]
        else:
            stack += input_str[:mid]
        answer = 'yes'

        for num in input_str[mid:]:
            if stack.pop() != num :
                answer='no'
                break
            
        print(answer)


solution()