package main

import (
	"fmt"
	"strings"
)

var (
	morseMap map[string]string
)

func demodulate(module_msg string) string {
	words := strings.Split(module_msg, " ")
	demodul_msg := ""

	for _, v := range words {
		_, has := morseMap[v]
		if !has {
			demodul_msg += "?"
		} else {
			demodul_msg += morseMap[v]
		}

	}

	return demodul_msg
}

func morseMapInit(regList []string) {
	for _, v := range regList {
		parsedReg := strings.Split(v, " ")
		if len(parsedReg) == 2 {
			morseMap[parsedReg[1]] = parsedReg[0]
		}
	}

}
func main() {

	morseMap = make(map[string]string, 0)
	testRegList := []string{"O ---", "S ..."}
	morseMapInit(testRegList)

	testCase := "... --- ..."
	fmt.Println("DeModulate ")
	fmt.Println(demodulate(testCase))

}
