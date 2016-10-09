package main

import (
	"fmt"
	"strconv"
)

var (
	Bucket []int
)

func InitVariable() {
	Bucket = make([]int, 5)
	/*	testCase		*/
	Bucket = []int{2, 9, 10, 21, 24}

}

/*			Insert Sorting		*/
func CustomSort(_bucket []int) {

	for i := 1; i < len(_bucket); i++ {
		max := _bucket[i]
		j := i
		for j > 0 && isBigger(max, _bucket[j-1]) {

			_bucket[j] = _bucket[j-1]
			j--

		}

		_bucket[j] = max
	}

	/*		Insert Sorting
	for i := 1; i < len(_bucket); i++ {
		max := _bucket[i]
		j := i
		for j > 0 && _bucket[j-1] < max {

			_bucket[j] = _bucket[j-1]
			j--

		}

		_bucket[j] = max
	}
	*/
}
func isBigger(a int, b int) bool {
	aStr := strconv.Itoa(a)
	bStr := strconv.Itoa(b)

	num1, _ := strconv.Atoi(aStr + bStr)
	num2, _ := strconv.Atoi(bStr + aStr)

	if num1 > num2 {
		return true
	} else {
		return false
	}

	/*
		if len(aStr) == len(bStr) {
			if a > b {
				return true
			} else {
				return false
			}

		} else {
			end := 0
			if len(aStr) > len(bStr) {
				end = len(bStr)
			} else {
				end = len(aStr)
			}
			idx := 0
			for idx < end {
				num1, _ := strconv.Atoi(string(aStr[idx]))
				num2, _ := strconv.Atoi(string(bStr[idx]))

				if num1 == num2 {
					idx++
				} else {
					if num1 > num2 {
						//fmt.Println("num1:", num1, "\tnum2:", num2)
						return true
					} else {
						return false
					}
				}
			}

			if len(aStr) < len(bStr) {
				return true
			} else {
				return false
			}
		}
	*/

}
func printAnswer(_bucket []int) {

	bigNumber := ""
	smallNumber := ""
	for _, v := range _bucket {
		bigNumber += strconv.Itoa(v)
	}

	for i := len(_bucket) - 1; i >= 0; i-- {

		smallNumber += strconv.Itoa(_bucket[i])
	}

	//fmt.Println(bigNumber)
	//fmt.Println(smallNumber)
	num1, _ := strconv.Atoi(bigNumber)
	num2, _ := strconv.Atoi(smallNumber)
	fmt.Println(num1 + num2)

}

func main() {
	InitVariable()
	CustomSort(Bucket)

	fmt.Println(Bucket)
	printAnswer(Bucket)

}
