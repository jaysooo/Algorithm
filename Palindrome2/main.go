package main

import "fmt"

func main() {
	inputStr := "onco"
	//fmt.Println(inputStr[len(inputStr)-3:])
	//fmt.Println(isPalindrome(inputStr[len(inputStr)-3:]))
	//fmt.Println(isPalindrome(inputStr))
	//return
	fmt.Println(getPalindrome(inputStr))
	//1.입력 받은 문자열이 팰린드롬인지 아닌지 검사한다. V
	//2.팰린 드롬이 아니라면 팰린드롬 규칙을 만족하는 문자열을 조합하여 만든다.
	//3.문자열의 끝에서부터 팰린드롬의 피봇 문자열을 찾는다.
	//4.중심을 기준으로 문자열의 끝까지 규칙을 만족하는 문자의 인덱스를 찾는다.
	//5.나머지 인덱스를 더해준다.
	//6.문자열 리턴

}

func isPal(str string) bool {
	start := 0
	isTrue := false
	end := len(str) - 1
	mid := len(str) / 2
	for start < mid {
		if str[start] == str[end] {
			start++
			end++
		} else {
			break
		}
	}

	if 
	return isTrue
}

func isPalindrome(str string) bool {
	isTrue := false
	i := 1
	if len(str) == 1 {
		isTrue = true
		return isTrue
	}

	p2 := len(str) / 2
	p1 := len(str) / 2
	if str[p1] == str[p2-1] {
		p1 = p1 - 1
	}
	fmt.Println(p1, p2)

	for (i <= p1) && (p2+i) <= len(str) && (p1-i) >= 0 {

		if str[p1-i] == str[p2+i] {
			i++
			fmt.Println("equal : ", i)
		} else {
			i--
			break
		}
	}

	if (p1-1)-i <= 0 {
		isTrue = true
	}
	fmt.Println(p1, "--", p2, "i = ", i)
	return isTrue
}

func getPalindrome(str string) int {
	needChars := -1

	cursor := len(str) - 3
	fmt.Println(cursor)
	for cursor > 0 {
		if isPalindrome(str[cursor:]) {
			fmt.Println("isPalindrome", str[cursor:])
			break
		} else {
			cursor--
		}
	}
	fmt.Println("fincal cursor ", oncn-1)
	return needChars
}
