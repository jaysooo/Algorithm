package main

import (
	"fmt"
)

func main() {
	fmt.Println("Start Run == ")

	// k := 7
	// arr := []int{0, 3, 4, 8, 10, 14, 18, 20, 22, 23, 25, 30, 33, 34, 36, 38, 39, 42}

	k := 4
	arr := []int{0, 1, 2, 5, 7, 9, 10, 12, 15}

	diffLoad(arr, k)

}

func diffLoad(_arr []int, _k int) {
	diffMap := make([]int, 0)

	//making Diff
	for i, _ := range _arr {
		if i == 0 {
			continue
		}

		if (_arr[i] - _arr[i-1]) > _k {
			fmt.Println("[E]")
		}
		diffMap = append(diffMap, _arr[i]-_arr[i-1])
	}
	getCount(diffMap, _k)

	// fmt.Println("result : ", getSimpleCount(diffMap, _k))

}

func getCount(_arr []int, _k int) {
	fmt.Println("getCount run ")
	resultMap := make([]int, 0)

	for i := 0; i < len(_arr); i++ {
		count := 1
		sum := 0
		cursor := 0
		for cursor < i {
			count++
			cursor++
		}
		for j := i; j < len(_arr); j++ {
			fmt.Println("currnet diff : ", _arr[j], "sum : ", sum)
			if (sum + _arr[j]) > _k {
				count++
				sum = _arr[j]
			} else {
				sum += _arr[j]
			}

		}
		resultMap = append(resultMap, count)
	}
	fmt.Println(resultMap)

}

func getSimpleCount(_arr []int, _k int) int {
	count := 1
	sum := 0
	for i := 0; i < len(_arr); i++ {
		fmt.Println("currnet diff : ", _arr[i], "sum : ", sum)
		if (sum + _arr[i]) > _k {
			count++
			sum = _arr[i]
		} else {
			sum += _arr[i]
		}
	}
	return count
}
