package main

import (
	"fmt"
	"strings"
)

var (
	words = []string{"H", "He",
		"Li", "Be", "B", "C", "N", "O", "F", "NE", "NA", "MG", "AL", "Si",
		"P", "S", "CI", "AR", "K", "CA", "SC", "Ti", "V", "Cr", "Mn", "Fe",
		"Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Br", "Kr",
		"Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
		"In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "Hf", "Ta", "W", "Re",
		"Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
		"Fr", "Ra", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl",
		"Lv", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho",
		"Er", "Tm", "Yb", "Lu", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
		"Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
	}
)

type dictionary struct {
	words []string
}

// func setAlchemDic(data map[string]dictionary, dataWord []string) {
// 	for _, v := range dataWord {
// 		_, has := data[string(v[0])]
// 		if !has {
// 			data[string(v[0])] = make([]string, 0)

// 		} else {

// 		}
// 	}
// }

func main() {
	// alchemDic := make(map[string]dictionary, 0)
	// setAlchemDic(alchemDic, words)

	//화학기호를 정렬한다.
	testCase := []string{
		"iamsimon",
		"international",
		"iamsmart",
		"iamchemist",
	}
	//문자열을 처음부터

	for _, T := range testCase {
		fmt.Println(isAlchemists(T))
	}

}
func isEqual(str string) bool {
	for _, v := range words {
		if strings.ToLower(v) == strings.ToLower(str) {
			return true
		}
	}
	return false
}

func isAlchemists(str string) bool {
	isTrue := false
	cursor := 0
	check := 0

	for cursor < len(str) {

		if isEqual(string(str[cursor])) {
			check++

		} else {
			if cursor+2 <= len(str) && isEqual(string(str[cursor:cursor+2])) {
				check = check + 2
			}
		}
		cursor++
	}
	if check >= len(str) {
		isTrue = true
	}
	return isTrue
}
