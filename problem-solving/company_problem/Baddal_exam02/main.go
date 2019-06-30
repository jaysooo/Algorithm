package main

import "fmt"

type Rect struct {
	x1, y1, x2, y2 int
}

func (r Rect) getArea() int {
	return (r.x2 - r.x1) * (r.y2 - r.y1)
}

func minusRect(a Rect, b Rect) Rect {

}

func main() {
	//var inputVal = []int{700, 400, 1600, 1100, 0, 400, 1100, 900, 900, 0, 1800, 650}

	r1 := Rect{700, 400, 1600, 1100}
	r2 := Rect{0, 400, 1100, 900}
	r3 := Rect{900, 0, 1800, 650}

	fmt.Println("r1 :", r1.getArea())
	fmt.Println("r2:", r2.getArea())
	fmt.Println("r3:", r3.getArea())

	//사각형 = 광고 영역
	//1,2,3번 사각형의 좌표를 받는다
	//각각의 사각형 객체를 만든다

	//1번 -2 번 = rs (사각형[])
	//rs -3 번 = rs (사각형[])
	//rs사각형의 광고비 출력
}
