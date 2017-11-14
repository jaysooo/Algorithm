package main

import (
	"fmt"
)

// 1.문자열의 길이가 맞는지 비교한다.
// 2.시작 인덱스와 엔드 인덱스를 구한다. (비교 최소화)쉬프트를 해야 하는 문자열의 규모를 구한다.
// 3.문자열을 스왑,쉬프트 하는 함수를 만든다
// 4.오른쪽 끝에서부터 같은 문자의 인덱스를 찾고 인덱스를 스왑후 나머지 문자는 왼쪽으로 스왑한다.
// 5.문자열의 규모를 줄인다.0이 될때 까지
func main() {
	aStr := "aabaaabbabbb"
	bStr := "abababababab"
	// aStr := "abab"
	// bStr := "aabb"

	//1.
	if len(aStr) != len(bStr) {
		fmt.Println("-1")
		return
	}
	//2.
	start := -1
	for start <= len(aStr) && aStr[start+1] == bStr[start+1] {
		start++
	}

	end := len(aStr)
	for end >= 0 && aStr[end-1] == bStr[end-1] {
		end--
	}
	converStr(aStr, bStr)
	// converStr(aStr[start+1:end], bStr[start+1:end])
}
func converStr(stra string, strb string) {
	endIdx := len(strb) - 1
	cnt := 0
	fmt.Println(endIdx)
	for endIdx > 0 {
		if strb[endIdx] == stra[endIdx] {
			endIdx--
		} else {

			ch := strb[endIdx]
			target := 0
			for i := endIdx; i > 0; i-- {
				if ch == stra[i] {
					target = i
					break
				}
			}
			chars := []rune(stra)

			for target < endIdx {
				tmp := chars[target]
				chars[target] = chars[target+1]
				chars[target+1] = tmp
				target++
				cnt++
			}

			stra = string(chars)

			fmt.Println("target Idx ", stra)

			endIdx--
		}

	}
	fmt.Println(stra, "cnt - ", cnt)
}
