import math

def set_test_case():
    input_str = input()
    convert_number = []
    for c in input_str:
        c = c.lower()
        number = ( ord(c) % 96) 
        dial_number = math.ceil(number/3)

        if c == 's' or c == 'v' or c=='z' or c == 'y':
            convert_number += [dial_number]
        else:
            convert_number += [dial_number+1]
            
    return convert_number
        
         


def solution():
    number = set_test_case()
    seconds = 0 
    for n in number:
       # print(n)
        seconds += (n + 1)
    print(seconds)
        



solution()