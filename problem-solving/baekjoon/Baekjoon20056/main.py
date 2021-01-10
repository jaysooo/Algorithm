

# class
    FireBall 파이어볼
       (variable)
           질량,
            방향,
            속력,
            위치(r, c)

    2-격자 클래스
       (variable)
            variable
            맵 크기
            파이어볼 갯수
#            파이어볼 리스트[]FireBall
            dictionry(K(r, c))--> (FireBall)
            남은 이동 횟수

        (method)
            turn() - 파이어볼 이동
            mergeAndivid() -  병합 및 분할 과정
                * 4개로 분할 후에는 이동이 이뤄나지 않는다. 다음 턴에서 이동함. -> 4개의 FireBall 객체 생성
            destroy()

            
# Global function
    getSpeedAfterMerge([]fireball) -
    getMassAfterMerge([]fireball) - 
    getdirectionAfterMerge([]fireball) - 
    checkSamePositionFireBall([] FireBall) - 
    getOutOfRange(c, r, d, s) - 격자 범위를 벗어날 경우 위치 정보 리턴

