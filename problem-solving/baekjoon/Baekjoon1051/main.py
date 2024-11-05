def set_test_case():
    input_str = input().split(" ")
    n,m = int(input_str[0]),int(input_str[1])
    rectangle = []
    for i in range(n):
        row = input()
        rectangle.append(row)

    return n,m,rectangle

def get_max_area(rectangle,x,y):
    distance= 0
    max_area = 0
    while (x+distance) < len(rectangle) and (y+distance) < len(rectangle[0]):
        if (rectangle[x][y] == rectangle[x+distance][y] == rectangle[x][y+distance] == rectangle[x+distance][y+distance]):
            max_area = distance
        distance +=1
    return max_area+1

def solution():
    n,m,rectangle = set_test_case()
    answer = 0
    for i in range(n):
        for j in range(m):
            max_area = get_max_area(rectangle,i,j)
            if max_area > answer:
                answer = max_area

    print(answer*answer)



if __name__ == "__main__":
    solution()