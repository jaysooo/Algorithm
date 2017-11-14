package main

import "fmt"

func main() {
	N := 3
	alpaMap := [3][3]rune{}

	lv := 0
	for i := 0; i < N; i++ {
		if (i+1)%2 != 0 {
			lv++
		}
		for j := 0; j < N; j++ {
			alpaMap[i][j] = ' '
		}
	}
	alpa := 'A'
	for i := 0; i <= N; i++ {
		if i%2 != 0 {
			startIdx := lv - 1
			for j := 0; j < i; j++ {
				alpaMap[lv-1][startIdx] = alpa
				alpa++
				startIdx++
			}
			lv--
		}
	}

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			fmt.Print(string(alpaMap[j][i]))
		}
		fmt.Println()
	}

}
