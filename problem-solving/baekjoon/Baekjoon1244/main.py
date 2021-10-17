# -*- encoding: utf-8 -*-
#import sys
#input = sys.stdin.readline

def set_test_case():
    commands = []
    switch_size= int(input())
    switch = input().split(' ')   
    switch = [int(x) for x in switch] 

    command_num = int(input())
    for i in range(0,command_num):
        command = input().split(' ')
        #command = map(lambda x: int(x),command)
        commands+=[[int(x) for x in command]]

    return switch,commands


def switch_process(switch,gender,switch_pos):
    switch=switch
    switch_interval = switch_pos
    if switch_pos == 0 :
        return switch

    # 남자의 경우 입력처리
    if gender == 1:
        while(switch_pos > 0 and switch_pos <= len(switch)):

            switch[switch_pos-1] = switch[switch_pos-1] ^ 1  # XOR 연산, index -1 처리
            switch_pos+=switch_interval   # 배수 처리 

    # 여자의 경우 입력처리
    elif gender == 2:
        symmetry = True     #대칭 여부의 flag 변수
        l =switch_pos -2  # 대칭점 기준 왼쪽 포인터
        r = switch_pos  # 대칭점 기준 오른쪽 포인터
        
        switch[switch_pos-1] = switch[switch_pos-1] ^ 1  # 대칭 여부와 상관없이, 대칭점의 스위치는 전환

        while(symmetry and l >= 0 and r < len(switch)): # 대칭되는 스위치를 찾는 범위가 리스트의 범위를 벗어나지 않는 조건

            if switch[l] == switch[r]:
                switch[l] = switch[l] ^ 1
                switch[r] = switch[r] ^ 1
                l -= 1
                r += 1    
            else:
                # 대칭되지 않는 조건
                symmetry=False

    # 입력 케이스 예외처리 부분
    else:
        #exception
        pass
    return switch

def solution(switch,commnads):
    for command in commnads:
        gender,pos = command[0],command[1]
        switch = switch_process(switch,gender,pos)
    
    # 최대 출력 스위치 조건을 만족하기 위한 처리
    num_by_line = 20
    for i in range(0,len(switch),num_by_line):
        print(*switch[i:i+num_by_line],sep=' ')


def main():
    switch,commands = set_test_case()
    solution(switch,commands)

if __name__ == '__main__':
    main()

