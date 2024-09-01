
def set_test_case():
    n = int(input())
    input_str = input().split(" ")
    arr = []
    input_str = list(map(int,input_str))
    for i,v in enumerate(input_str):
        arr += [(v,(i+1))]

    return arr

def solution():
    arr = set_test_case()
    sorted_arr = sorted(arr, key=lambda x: x[1], reverse=True)
    sorted_arr = sorted(sorted_arr, key=lambda x: x[0], reverse=False)
    answer = [0] * len(sorted_arr)

    for item in sorted_arr:
        cursor = 0
        height = item[1]
        cnt = item[0]
        while cursor < len(arr) and answer[cursor] > 0 and cnt > 0 :
            if answer[cursor] > height :
                cnt -=1
            cursor += 1
        temp = answer[cursor:-1]
        answer[cursor] = height
        answer[cursor+1:] = temp

    answer = list(map(str,answer))
    print(" ".join(answer))


if __name__ == '__main__':
    solution()