
input = 121

def answer(arr, start, end):
    if start >= end:
        return 1

    if (arr[start] == arr[end]):
        return answer(arr, start+1, end-1)
    else:
        return 0

# 1 = palindrome
# 0 = Not Palindrome

def solution1(num):
    divide = 1
    arr = []
    while (True):
        if int(num/divide) == 0:
            break

        quo = int(num/divide)
        print(quo)
        divide = divide*10
        arr.append(quo % 10)

    print(arr)
    print(answer(arr, 0, len(arr)-1))

solution1(input)

