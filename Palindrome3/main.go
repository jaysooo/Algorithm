package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println("[LOG] Palindrome Division Start")
	defer fmt.Println("[LOG] Palindrome Division Done")

	// //테스트 케이스
	// T := make([]string, 0)
	// T = append(T, "bceffecbzzz")
	// T = append(T, "j")
	// T = append(T, "oncoder")
	// T = append(T, "yhcahxs")
	// T = append(T, "askjasccsaeeeee")
	// T = append(T, "eabbace")
	// for _, v := range T {
	// 	MinPalindromeList(v)
	// }
	
	rs := ""
	testStr := "asdfljdslakfsdafkjladskjflksajsadjlkfafjdslakjfklasjflsjadjlekwwlekfjlwkejflkewjflkewjfkjlweklfjweljflwekjfklejwflkjwelfkjwelkjflkwejflkewjflkjwelkfjewkljflkewjflkwejlkfjwlekjflkwejflkjwefljkewklfjweklfjlkewjfkljwekfljweklfjwelkjfklwjefkljweklfjwekljfsajdf;aksjfskdjf;osej;foksdjf;lksdjf;osaiejf;lksdjf;lskjf;aoeskjf;osjfos;aiejfa;sokjfdlsknvkznvzksdjvnoweinveo;inbo;isf;oisj;ovieno;zsijfo;seijfsenvoeinvoszijves;oijv;sozkfjs;oezifjse;oifjsz;oijvozisevo"
	rs += testStr

	for i := 0; i < 5; i++ {
		rs += testStr
	}
	MinPalindromeList(rs)
}
func MinPalindromeList(input string) {
	//팰린드롬의 결과를 저장할 리스트
	list := make([]string, 0)
	tmp := input
	for i := len(tmp); i > 0 && len(tmp) > 0; i-- {
		start := 0
		for start+i <= len(tmp) {
			word := tmp[start : start+i]
			if CheckPalind(word) {
				//팰린드롬 저장
				list = append(list, word)
				//해당 팰린드롬을 제외하고 저장
				pivot := strings.Index(tmp, word)
				tmp = tmp[0:pivot] + tmp[pivot+len(word):]
			} else {
				start++
			}
		}
	}

	fmt.Print("[LOG] RESULT")
	//결과 출력
	for i := 0; i < len(list); i++ {
		fmt.Print("[ " + list[i] + " ] ")
	}
	fmt.Println("\tMinimum : :", len(list))
}

//팰린드롬인지 여부 검사
func CheckPalind(str string) bool {
	//fmt.Println("Check : ", str)
	i := 0
	j := len(str) - 1
	for i < j {
		if str[i] == str[j] {
			i++
			j--
		} else {
			break
		}
	}
	if i >= j {
		return true
	} else {
		return false
	}
}
