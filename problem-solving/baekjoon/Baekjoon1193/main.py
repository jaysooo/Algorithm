
import abc


def solution():
    x = int(input())
    i = sum = numerator = denominator = 0

    while(sum <= x):
        if sum + i >= x:
            b = (x - sum)
            a = (i - b) + 1
            break
        else:
            sum +=i
            i += 1
        

    if i % 2 == 0 :
        numerator = b
        denominator = a
    else:
        numerator = a
        denominator = b
    
    print(f'{numerator}/{denominator}')

solution()

    