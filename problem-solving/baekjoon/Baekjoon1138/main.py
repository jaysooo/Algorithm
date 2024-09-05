# Main Idea :
# 	- 정답을 편하게 구하기 위해 자료구조를 만든다
# 		(lt,height)
# 		* lt = 왼쪽 방향으로 키가 큰 사람 수
# 		* height = 키
# 	- lt,height 순서로 정렬 한다.
# 	- 정답 배열을 만든다
# 	- 정답 배열에 lt 조건 대로 height 를 저장한다
# 	- lt 조건에 맞는지 체크하면서, 정답 배열에 들어갈 위치(cursor)를 구한다.
# 	- 정답 배열에 원소 추가
# 		- 위치(cursor) 기준으로 오른쪽 배열 복제.
# 		- 정답배열 위치(cursor)에 원소를 추가하고 + 오른 쪽 배열 복제본 복사
def set_test_case():
    n = int(input())
    input_str = input().split(" ")
    arr = []
    input_str = list(map(int,input_str))
    for i,v in enumerate(input_str):
        arr += [(v,(i+1))]

    return arr

def solution():
    # 테스트 케이스 입력
    arr = set_test_case()

    # 왼쪽 방향 자기보다 키 큰 사람의 수 기준으로 정렬
    sorted_arr = sorted(arr, key=lambda x: x[1], reverse=True)
    # 키 큰 사람의 수가 동일할 경우 키가 큰 사람 기준으로 내림 차순 정렬
    sorted_arr = sorted(sorted_arr, key=lambda x: x[0], reverse=False)
    # 정답 배열 선언
    answer = [0] * len(sorted_arr)


    for item in sorted_arr:
        cursor = 0
        height = item[1]
        cnt = item[0]
        #lt 조건에 맞는지 체크하면서, 정답 배열에 들어갈 위치(cursor)를 찾음
        while cursor < len(arr) and answer[cursor] > 0 and cnt > 0 :
            if answer[cursor] > height :
                cnt -=1
            cursor += 1
        # 정답 배열에 원소 추가
        right_part = answer[cursor:-1]
        answer[cursor] = height
        answer[cursor+1:] = right_part

    # 정답 출력
    answer = list(map(str,answer))
    print(" ".join(answer))


if __name__ == '__main__':
    solution()