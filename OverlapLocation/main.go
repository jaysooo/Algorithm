package main

import (
	"fmt"
)

type Range struct {
	startPoint int
	endPoint   int
}
type PointInfo struct {
	pointPos int
	ref      int
}

var (
	PointMap     []Range
	overlapTable [6]PointInfo
	idx          int
)

func mapSet(_pointMap []Range) {
	for _, v := range _pointMap {
		startRefBit := 0
		endRefBit := 0
		for _, k := range _pointMap {
			if v.startPoint >= k.startPoint && v.startPoint <= k.endPoint {
				startRefBit++
			}
			if v.endPoint >= k.startPoint && v.endPoint <= k.endPoint {
				endRefBit++
			}
		}

		overlapTable[idx] = PointInfo{v.startPoint, startRefBit}
		idx++
		overlapTable[idx] = PointInfo{v.endPoint, endRefBit}
		idx++
	}
}

func answerPrint(_overlapTable [6]PointInfo) {

	// 정렬 후
	// 가장 첫번째 점 출력
	// 가장 마지막 점 출력
	// ref 비트가 짝수인 구간에서 구간을 짧게 해서 출력
	// ref 비트가 홀수인구간에서 출력

}

func main() {
	fmt.Println("Start")

	PointMap = []Range{
		Range{startPoint: 1, endPoint: 3},
		Range{startPoint: 2, endPoint: 4},
		Range{startPoint: 5, endPoint: 6},
	}

	mapSet(PointMap)

	answerPrint(overlapTable)
	for i, v := range overlapTable {
		fmt.Println(i, " : ", v)
	}

}
