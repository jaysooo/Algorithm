package main

import (
	"fmt"
	"time"
)

//데이트
type FDate struct {
	month string
	day   string
}
type FlowerType struct {
	startD  time.Time
	endD    time.Time
	betDays int
}

var (
	Cursor       int //가든 커서
	Garden       []FlowerType
	Bucket       []FlowerType
	FestivalInfo FlowerType
	layout       = "2006-01-02"
)

func getFDateType(mon1 string, day1 string, mon2 string, day2 string) (time.Time, time.Time, int) {
	t1, _ := time.Parse(layout, "2016-"+mon1+"-"+day1)
	t2, _ := time.Parse(layout, "2016-"+mon2+"-"+day2)
	return t1, t2, int(t2.Sub(t1).Hours() / 24)
}

func Init() {
	Cursor = -1
	FestivalInfo.startD, FestivalInfo.endD, FestivalInfo.betDays = getFDateType("03", "01", "11", "30")
	Bucket = make([]FlowerType, 0)
	Garden = make([]FlowerType, 0)

	/*	 버킷 초기화	*/

	var flower FlowerType
	flower.startD, flower.endD, flower.betDays = getFDateType("01", "01", "05", "31")
	Bucket = append(Bucket, flower)

	var f2 FlowerType
	f2.startD, f2.endD, f2.betDays = getFDateType("01", "01", "06", "03")
	Bucket = append(Bucket, f2)

	var f3 FlowerType
	f3.startD, f3.endD, f3.betDays = getFDateType("05", "15", "08", "31")
	Bucket = append(Bucket, f3)

	var f4 FlowerType
	f4.startD, f4.endD, f4.betDays = getFDateType("06", "10", "12", "10")
	Bucket = append(Bucket, f4)
}

func con1Check(t1 time.Time, t2 time.Time) bool {

	return t1.After(t2)
}

func main() {
	Init()

	for i, v := range Bucket {
		if len(Garden) == 0 {

			if Bucket[i].startD.Before(FestivalInfo.startD) {
				Garden = append(Garden, v)
				Cursor++
			}

		} else {

			if Bucket[i].startD.Before(Garden[Cursor].endD) {
				Garden = append(Garden, v)
				Cursor++
			}

		}

		if Garden[Cursor].endD.After(FestivalInfo.endD) {
			fmt.Println("Answer : ", Cursor)
			fmt.Println(Garden)
			break
		}
	}

}
