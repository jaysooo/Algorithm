package main

import (
	"fmt"
	"strconv"
)

var (
	Bucket []int
)

func InitVariable() {

	/*	testCase		*/
	// Bucket = make([]int, 5)
	// Bucket = []int{9, 2, 13, 7, 24}
	Bucket = make([]int, 7)
	Bucket = []int{20, 16, 10, 45, 30, 28, 47}
}

/*			Insert Sorting		*/
func CustomSort(_bucket []int) {

	//		Insert Sorting
	for i := 1; i < len(_bucket); i++ {
		max := _bucket[i]
		j := i
		for j > 0 && _bucket[j-1] > max {

			_bucket[j] = _bucket[j-1]
			j--
		}
		_bucket[j] = max
	}

}
func getMinPoints(_bucket []int) string {
	a1 := _bucket[0]
	a2 := _bucket[1]
	idx := 1
	for idx < (len(_bucket) - 1) {
		if (a2 - a1) > (_bucket[idx+1] - _bucket[idx]) {
			a1 = _bucket[idx]
			a2 = _bucket[idx+1]
		} else if (a2 - a1) == (_bucket[idx+1] - _bucket[idx]) {
			if (a1 + a2) > (_bucket[idx+1] + _bucket[idx]) {
				a1 = _bucket[idx]
				a2 = _bucket[idx+1]
			}
		}
		idx++
	}
	return strconv.Itoa(a1) + " , " + strconv.Itoa(a2)
}
func main() {
	fmt.Print("In : ")
	InitVariable()
	CustomSort(Bucket)
	for _, v := range Bucket {
		fmt.Print(v, " ")
	}

	fmt.Println("\nOut : ", getMinPoints(Bucket))
}
