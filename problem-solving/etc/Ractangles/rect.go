package main

import (
	"fmt"
)

//사각형 구조체 정보
type Rect struct {
	//좌변하단 꼭지점
	x1 int
	y1 int
	//우변상단 꼭지점
	x2 int
	y2 int
	//넓이
	area int
}

//사각형 객체 생성 함수
func newRect(x1 int, y1 int, x2 int, y2 int) *Rect {
	node := new(Rect)
	node.x1 = x1
	node.x2 = x2
	node.y1 = y1
	node.y2 = y2
	node.area = (x2 - x1) * (y2 - y1)
	return node
}

//사각형 r2가 r1을 포함하고 있는지 비교
func isIncludeRect(r1 *Rect, r2 *Rect) bool {
	include := false
	fmt.Println(r2, "와 ", r1, "을 비교 ")
	if (r1.x1 > r2.x1 && r2.x2 > r1.x2) && (r1.y1 > r2.y1 && r2.y2 > r1.y2) {
		include = true
		fmt.Println(r2, "가 ", r1, "을 포함함 ")
	}

	return include
}
