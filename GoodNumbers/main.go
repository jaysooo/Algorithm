package main

import (
	"fmt"
)

func main() {
	testT := []int{1, 4, 2, 5, 6}

	solution(testT)

	fmt.Println("end")
}

func solution(arr []int) {
	for i := 2; i < len(arr); i++ {
		// //	fmt.Println(arr[:i])
		// fmt.Println(i)


		//숫자 세개로 조합할 수 있는 경우 = 배열에서 원소 3개를 가져와 조합
		for g := 0; g < i; g++ {
			for z := 0; z < i; z++ {
				for x := 0; x < i; x++ {

					if (arr[g] + arr[z] + arr[x]) == arr[i] {
						fmt.Println("GoodNumbers :", arr[i])
						break
					}
				}

			}
		}

	}

}
