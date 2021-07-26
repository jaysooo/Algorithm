
#입력 테스트 케이스 처리
def setTestCase():
    N=input()
    COMMAND_LIST = []
    for i in range(int(N)):
        COMMAND_LIST.append(input())
    return COMMAND_LIST

#커맨드 라인 파싱 
def command_parser(input_command_list):
    command_list = []
    for i in input_command_list:
        split_command = i.split(" ")
        command_type,command_content,seconds = split_command[0],split_command[1],int(split_command[2])
        command_list.append((seconds,command_content))
    
    return command_list


# 입력 처리 
def process_command(command_list):
    text = ''   # 결과 문자열을 담을 변수
    rollback_point=-1   # undo 의 분기를 찾을 카운트
    
    # 명령어는 역순으로 처리
    for command_set in reversed(list(command_list)):
        seconds,command = command_set
        # undo 가 적용되는 마지막 명령어 분기
        if seconds == rollback_point:       
            rollback_point = -1 
            continue
        # undo 가 해당되는 구간의 명령어 skip 분기
        elif rollback_point != -1 and seconds > rollback_point:
            continue
        # undo 명령어를 만났을 때 분기
        elif command.isdigit():
            rollback_point = seconds - int(command)
            if rollback_point < 0:
                rollback_point = 0
            continue
        # 문자 저장
        text+=command
    
    return text[::-1]   # 역순으로 결과 문자열이 저장되었기 때문에 reverse 처리 
        


def solution():
    input_command_list = setTestCase()
    command_list=command_parser(input_command_list)
    result = process_command(command_list)

    print(result)

if __name__=='__main__':
    solution()