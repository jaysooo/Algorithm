package main

import "fmt"

func main() {
	coinTypes []int{1,5,10}
	rec(4)
}
func recursive(data []int,price int){
	if data.length < 1
		return 0

	if price < 0 
		return 0

	if price == 0
		return 1

	return recursive(data[:-1],price)+recursive(data[max],price-data[max])

}
func rec(n int) int {
	fmt.Println(n)
	if n < 1 {
		return 1
	}
	return n * rec(n-1)
}
