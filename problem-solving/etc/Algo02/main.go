package main

import (
	"fmt"
)

//빛의 방향 정의
// 1=왼쪽에서 날라옴
// 2=아래쪽 에서 날라옴
// 3=오른쪽
// 4=위쪽
const (
	left       = 1
	down       = 2
	right      = 3
	up         = 4
	lMirror    = 1
	rMirror    = 2
	noneMirror = 0
)

var (
	cnt = 0
)

func nextRoom(_x int, _y int, roomType int, lightDirection int) (int, int, int) {
	//방이 없는 경우
	if roomType == noneMirror {
		if lightDirection == left {
			_y = _y + 1
			return _x, _y, lightDirection
		}
		if lightDirection == right {
			_y = _y - 1
			return _x, _y, lightDirection
		}
		if lightDirection == down {
			_x = _x - 1
			return _x, _y, lightDirection
		}
		if lightDirection == up {
			_x = _x + 1
			return _x, _y, lightDirection
		}
		//문자1  타입 방
	} else if roomType == lMirror {
		if lightDirection == left {
			_x = _x - 1
			lightDirection = up
			return _x, _y, lightDirection
		}
		if lightDirection == right {
			_x = _x + 1
			lightDirection = down
			return _x, _y, lightDirection
		}
		if lightDirection == down {
			_y = _y - 1
			lightDirection = right
			return _x, _y, lightDirection
		}
		if lightDirection == up {
			_y = _y + 1
			lightDirection = left
			return _x, _y, lightDirection
		}
		//문자 2 타입 방
	} else if roomType == rMirror {
		if lightDirection == left {
			_x = _x + 1
			lightDirection = down
			return _x, _y, lightDirection
		}
		if lightDirection == right {
			_x = _x - 1
			lightDirection = up
			return _x, _y, lightDirection
		}
		if lightDirection == down {
			_y = _y + 1
			lightDirection = left
			return _x, _y, lightDirection
		}
		if lightDirection == up {
			_y = _y - 1
			lightDirection = right
			return _x, _y, lightDirection
		}
	}
	return -1, -1, -1
}
func isOutOfRangeRoom(_x int, _y int, _N int) bool {
	if _x < 0 || _y < 0 || _x >= _N || _y >= _N {
		return true
	} else {
		return false
	}
}
func getMirrorRoomCnt(room [][]int, n int) int {
	cnt := 0
	if room[0][0] > 0 {
		cnt++
	}
	x, y, l := nextRoom(0, 0, room[0][0], 1)
	fmt.Println(" X = ", x, " Y = ", y, "Light Direction = ", l, "currentRoom :", room[x][y], "cnt:", cnt)

	if room[x][y] > 0 {
		cnt++
	}

	for true {
		x, y, l = nextRoom(x, y, room[x][y], l)
		fmt.Println(" X = ", x, " Y = ", y, "Light Direction = ", l, "currentRoom :", room[x][y], "cnt:", cnt)

		if isOutOfRangeRoom(x, y, n) {
			return cnt
		}
		if room[x][y] > 0 {
			cnt++
		}
		fmt.Println(" X = ", x, " Y = ", y, "Light Direction = ", l, "currentRoom :", room[x][y], "cnt:", cnt)

	}

	return cnt
}
func main() {
	fmt.Println("Algorithm Start")
	// N := 2
	// sampleRoom := [][]int{{0, 2}, {1, 1}}
	// fmt.Println(getMirrorRoomCnt(sampleRoom, N))
	cnt = 0
	N := 3
	sampleRoom := [][]int{{2, 0, 1}, {2, 2, 0}, {2, 1, 0}}
	fmt.Println(getMirrorRoomCnt(sampleRoom, N))

}
