package main

import (
	"fmt"
)

var (
	T          int //테스트 케이스 입력 수
	N          int
	M          int
	K          int
	container  []*Rect
	hasRectCnt int //포함돈 사각형의 개수
)

//N,M,K 입력
func inputNmk() (int, int, int) {
	n, m, k := 0, 0, 0
	fmt.Scanln(&n, &m, &k)
	return n, m, k
}

//사각형 정력보 입력
func inputRectPoint() (int, int, int, int) {
	x1, y1, x2, y2 := 0, 0, 0, 0

	fmt.Scanln(&x1, &y1, &x2, &y2)

	return x1, y1, x2, y2
}

//넓이 순서로 내림차순 정렬
func orderRect(list []*Rect) {

	//선택 정렬
	for i := 0; i < len(list); i++ {

		for j := i + 1; j < len(list); j++ {
			if list[i].area < list[j].area {
				idx := j
				tmp := &Rect{0, 0, 0, 0, 0}
				tmp = list[i]
				list[i] = list[idx]
				list[idx] = tmp
			}
		}
		//j 와 스왑
		//tmp := &Rect{list[i].x1, list[i].y1, list[i].x2, list[i].y2}

	}
	//	fmt.Println(list)

}

func calculateRect(list []*Rect) {
	qu := NewQueue(1)
	fmt.Println(list)
	for i := 0; i < len(container); i++ {
		cnt := 1                   //포함된 사각형 개수
		targetRect := container[i] //비교 대상의 사각형

		//큐에 사각형 삽입
		for j := i + 1; j < len(container); j++ {
			qu.Push(container[j])
		}
		//큐안에 모든 사각형 비교
		for !qu.IsEmpty() {
			r := qu.Pop()
			//사각형의 넓이가 타겟보다 작고 포함하는지 검사
			if (r.area < targetRect.area) && (isIncludeRect(r, targetRect)) {
				targetRect = r
				cnt++ //포함하고 있는 개수 증가
			}
		}

		//사각형 최대 포함 개수 갱신
		if hasRectCnt < cnt {
			hasRectCnt = cnt
		}
	}

}

func main() {

	/*
		//data := newRect(1, 1, 2, 2)
		//fmt.Println(data)
			s := NewStack()
			s.Push(newRect(1, 1, 2, 2))
			s.Push(newRect(2, 2, 4, 4))
			fmt.Println(s.Pop())
	*/

	//Test T 입력
	fmt.Println("[LOG] SCPC Rect Start..")
	T = 1
	container = make([]*Rect, 0)

	//fmt.Scanf("%d", &T)

	//T 만큼 프로그램 반복
	for i := 0; i < T; i++ {
		//N,M,K 를 입력
		//N, M, K = inputNmk()
		N = 10
		M = 8
		K = 5
		for i := 0; i < K; i++ {
			//K 갯수 사각형 두 꼭지점을 입력
			x1, y1, x2, y2 := inputRectPoint()
			//컨테이너에 저장
			container = append(container, newRect(x1, y1, x2, y2))
		}
		//컨테이너에 저장된 사각형의 넓이를 기준으로 내림정렬
		orderRect(container)
		calculateRect(container)
	}
	fmt.Println(hasRectCnt)
}

/*
10 8 5
1 1 10 7
2 2 5 6
3 2 9 5
6 3 8 4
6 0 9 8

*/
