package main

import (
	"fmt"
)

var (
	dic map[string]interface{} //중복 문자열을 저장 할 맵
	T   int
	cnt int
)

func Init() {
	dic = make(map[string]interface{})
}

func Analysis(in string) {

	end := len(in) //문자열의 끝 인덱스

	for i := 1; i < end; i++ {
		size := 1 //시작 증감 크기

		for (i+size < end) && (i-size >= 0) {

			s_cur := i //시작 커서
			e_cur := i //끝 커서

			/*
				if in[i] == in[i+1] { //같은 문자가 연속적으로 붙어 있는 경우
					e_cur = i + 1
					rs := in[s_cur : e_cur+1]
					_, has := dic[rs]
					if !has {
						dic[rs] = true
					}
				}
			*/
			cnt++
			if in[e_cur+size] == in[s_cur-size] {
				rs := in[s_cur-size : e_cur+size+1]

				_, has := dic[rs]
				if !has {
					dic[rs] = true
				}
				size++
			} else { //문자가 다를 경우 루프 탈출
				break
			}
		}

		size = 1
		for (i+size < end) && (i-size >= 0) {

			s_cur := i //시작 커서
			e_cur := i //끝 커서
			cnt++
			if in[i] == in[i+1] { //같은 문자가 연속적으로 붙어 있는 경우
				e_cur = i + 1
				rs := in[s_cur : e_cur+1]
				_, has := dic[rs]
				if !has {
					dic[rs] = true
				}
			}
			cnt++
			if e_cur == end-1 {
				break
			}
			if in[e_cur+size] == in[s_cur-size] {
				rs := in[s_cur-size : e_cur+size+1]

				_, has := dic[rs]
				if !has {
					dic[rs] = true
				}
				size++
			} else { //문자가 다를 경우 루프 탈출
				break
			}
		}
	}

}
func PrintResult() {

	for i, _ := range dic {
		fmt.Printf("[%s] ", i)
	}
	fmt.Printf(", %d\n", len(dic))

}

func main() {
	Init()
	cnt = 0
	//_, err := fmt.Scanln(&N)
	/*
		if err != nil {
			fmt.Println("[E]", err)
			return
		}
	*/
	T = 1
	input := "DDD"
	//input := "IAEFGSADAOFSOSPIPOKTOOOTSCIVIC"
	//input := "ILOVECOMPUTER"
	//input = "TOOTSDS"

	for i := 0; i < T; i++ {

		//fmt.Scanln(&input)
		Analysis(input)
		PrintResult()

	}
	fmt.Println("Loop Cnt:", cnt)

}
