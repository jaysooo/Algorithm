package main

import (
	"fmt"
)

var (
	N         = 2 //호수의 수개
	M         = 4 //일기 예보 일수
	T         = 1 //테스트 케이스 개수 T
	RainyDays = 0
)

func main() {
	//fmt.Scanln(&T)
	//	fmt.Scanln(&N, &M)
	//	fmt.Println(N, M, T)

	/*		호수 초기화		*/
	RainyDays = 0
	N = 3
	M = 6
	lakeInfo := make([]int, N+1)
	foreCastSchedule := []int{0, 1, 2, 0, 0, 0}
	setLakeInfo(lakeInfo, foreCastSchedule)

	/*		홍수의 여부 검사		*/
	if haveFlood(foreCastSchedule) {
		fmt.Println("NO")
	} else {
		printResult(foreCastSchedule)
	}

}

func printResult(_sch []int) {

	seq := len(_sch) - 1

	for seq >= 0 {
		if _sch[seq] != 0 {
			for i := seq; i >= 0; i-- {
				if _sch[i] == 0 {
					_sch[i] = _sch[seq] * -1
					seq = i
					minusCnt++
					break
				}
			}
		}
		seq--
	}

	fmt.Println("YES")
	for _, v := range _sch {

		if v < 0 {
			fmt.Printf("%d ", v*-1)
		} else if v == 0 {
			fmt.Printf("%d ", v)
		}
	}

	fmt.Println()

}

func haveFlood(_sch []int) bool {
	cnt := 0
	isFlood := false
	for i, v := range _sch {
		if v == 0 {
			cnt++
		}
		if i > 0 && v > 0 {
			if _sch[i-1] == _sch[i] {
				isFlood = true
			}
		}
	}
	if cnt < RainyDays {
		//	fmt.Println("RaniyDays : ", RainyDays, "Cnt : ", cnt)
		isFlood = true
	}

	return isFlood
}
func setLakeInfo(_info []int, sch []int) {

	for _, v := range sch {
		if v > 0 {
			_info[v]++
			RainyDays++
		}
	}
}
