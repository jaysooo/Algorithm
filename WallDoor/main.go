package main

import (
	"fmt"
)

var (
	WallWidth       int    //벽장 길이
	WallMap         []bool //벽장의 문 상태 정보			true = open     false = closed
	OpenWallList    []int  //문이 열릴 위치 정보
	OpendedWallNum1 int    //현재 열린 문1치의 위치 정보
	OpendedWallNum2 int    //현재 열린 문2의 위치 정보
)

func main() {
	fmt.Println("=====JSS Solving Start=====")

	/*  옷장의 길이를 입력 및 초기화
	n, _ := fmt.Scanf("%d", &WallWidth)
	if n < 1 {
		fmt.Println("[E] Wall Width Input Error ")
		return
	}
	*/
	WallWidth = 7
	WallMap = make([]bool, WallWidth)

	/* 문이 열려 있는 위치 정보 입력 		*/
	OpendedWallNum1, OpendedWallNum2 = 1, 4

	/*
		fmt.Scanf("%d %d", &c1, &c2)
	*/

	WallMap[OpendedWallNum1] = true
	WallMap[OpendedWallNum2] = true
	fmt.Println("==초기맵==")
	for _, v := range WallMap {
		fmt.Printf(" %v ", v)
	}
	fmt.Println()
	fmt.Println()
	/*		벽장 문을 열 횟수 정보 입력 		*/

	toOpenCnt := 4
	/*
		fmt.Scanf("%d", &toOpenCnt)
	*/

	OpenWallList = make([]int, toOpenCnt)

	/*	 문을 열 순서 정보 입력 		*/
	/*
		for i := 0; i < toOpenCnt; i++ {
			wallIdx := 0
			fmt.Scanf("%d", &wallIdx)
			OpenWallList[i] = wallIdx
		}
	*/
	//예제
	OpenWallList[0] = 2
	OpenWallList[1] = 0
	OpenWallList[2] = 5
	OpenWallList[3] = 4

	/*	최소 이동 거리   	*/
	fmt.Println("문의 이동 거리 : ", GetTotalMoveWall())
}

func GetShortedOpendWallIdx(targetWall int) int {

	rs1 := targetWall - OpendedWallNum1
	if rs1 < 0 {
		rs1 *= -1
	}
	rs2 := targetWall - OpendedWallNum2
	if rs2 < 0 {
		rs2 *= -1
	}

	//fmt.Println("rs1:", rs1, "rs2:", rs2, "Wall1:", OpendedWallNum1, "Wall2:", OpendedWallNum2)
	if rs1 <= rs2 {

		return OpendedWallNum1

	} else {

		return OpendedWallNum2
	}

}

func SwapWallDoor(opendWall int, targetWall int) int {

	WallMap[targetWall] = true
	WallMap[opendWall] = false

	//열린 문의 정보 위치 정보 갱신
	if opendWall == OpendedWallNum1 {
		OpendedWallNum1 = targetWall
		//fmt.Println("현재 열린 문의 위치1 : ", OpendedWallNum1)
	} else {
		OpendedWallNum2 = targetWall
		//fmt.Println("현재 열린 문의 위치2 : ", OpendedWallNum2)
	}

	fmt.Println("==현재 벽의 상태 ==")
	for _, v := range WallMap {
		fmt.Printf(" %v ", v)
	}
	fmt.Println()

	//문의 이동 횟수
	rs := targetWall - opendWall

	if rs < 0 {
		rs *= -1
	}

	return rs

}

func GetTotalMoveWall() int {
	TotalMoveWallCnt := 0 //문의 이동 횟수를 0으로 초기화

	for _, v := range OpenWallList {

		//현재 가장 까까이 닫힌 문의 인덱스를 받아옴
		OpenWallIdx := GetShortedOpendWallIdx(v)
		//열린 문의 이동
		fmt.Println("이동해야 할 문의 인덱스 : ", OpenWallIdx)
		//문의 이동 횟수 증가
		TotalMoveWallCnt += SwapWallDoor(OpenWallIdx, v)
	}

	return TotalMoveWallCnt
}
