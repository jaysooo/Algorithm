
# Main Idea
# 1) 입력 테스트 케이스의 데이트 문자열 타입을 처리하기 편한 초 단위로 변환
# 2) 점수를 낸 로그를 반복문으로 돌면서, 점수를 낸 직전 스코어의 승자 팀이 있는 경우 1팀과 2팀의 이긴 시간을 누적 저장
# 3) 마지막에는 승팀의 존재 여부를 확인하고, 이긴 시간을 추가 보정

# 입력 데이터 파싱
def set_test_case():
    n = int(input())
    score_log = []
    for i in range(n):
        input_str= input().split(" ")
        team = int(input_str[0])
        score_time_str = input_str[1].split(":")
        minutes = int(score_time_str[0])
        seconds = int(score_time_str[1])

        total_seconds = minutes * 60 + seconds
        score_log += [[team,total_seconds]]

    return score_log
def get_winner(a_score,b_score):
    return 0 if a_score > b_score else 1

def get_format_answer(seconds):
    minutes = seconds //60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"
def solution():
    score_log  = set_test_case()
    current_score = [0,0] # 1, 2팀의 누적 점수
    last_winner = -1
    answer = [0,0] # 1,2 팀의 정답출력을 위한 리스트

    for idx,t in enumerate(score_log):

        # 이전 스코어가 동점이 아닌경우 계산
        if current_score[0] != current_score[1] :
            last_winner = get_winner(current_score[0], current_score[1])
            answer[last_winner] += t[1]-score_log[idx-1][1]

        # 누적 점수 저장
        if t[0] == 1:
            current_score[0] +=1
        else:
            current_score[1] +=1

    if current_score[0] != current_score[1]:
        last_winner = get_winner(current_score[0], current_score[1])
        answer[last_winner] += 60*48 - score_log[-1][1]

    print(get_format_answer(answer[0]))
    print(get_format_answer(answer[1]))

if __name__=='__main__':
    solution()