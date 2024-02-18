

def set_test_case():
    T = int(input())
    rectangles = []
    for i in range(T):
        in_temp = input().split(" ")
        r = [int(in_temp[0]),int(in_temp[1])]
        rectangles.append(r)

    return rectangles

def solution():
    size = 10
    max_size = 100
    area = 0

    matrix = [[0 for i in range(max_size)] for j in range(max_size)]
    rectangles= set_test_case()

    # 색종이 영역 마킹
    for rectangle in rectangles:
        for j in range(rectangle[0],rectangle[0]+size):
            for k in range(rectangle[1],rectangle[1]+size):
                matrix[j][k] = 1

    # 색종이 영역 완전 탐색 = 배열 요소 1은 1X1 의 넓이로 본다.
    for i in range(max_size):
        for j in range(max_size):
            if matrix[i][j] == 1:
                area+=1

    print(area)

if __name__ == '__main__':
    solution()
