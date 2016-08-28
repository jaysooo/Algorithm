package main

import (
	"fmt"
)

func main() {
	str := "test Hello World"
	tmp := str[0:4]

	fmt.Println(len(str))
	fmt.Println(len(tmp))

	//fmt.Println(tmp[0:10])
}
