
# 1. valid_check 
#   - 폴리오미노 유효성 검사 
#   - x 가 짝수개수인지 체크 
# 2. custom_split
#   - X와 . 을 분리 
# 3. convert
#   - 

def set_test_case():
    T = input()
    return T

def valid_check(s):
    result = True
    for case in s.split('.'):
        case_len = len(case)
        if case_len %2 != 0:
            result = False
            return result

    return result

def custom_split(input_str):
    split_list = []

    last_dot_point=-1
    cursor = 0 

    while (cursor < len(input_str)):

        # 첫번째 문자가 닷(.) 이 아닌 경우 ,  연속적인 닷(.)이 아닌경우 
        if input_str[cursor] == '.':
            if cursor > 0 and not (input_str[cursor-1] == '.'):
                split_list.append(input_str[last_dot_point+1:cursor])
                last_dot_point = cursor
            else:
                last_dot_point = cursor
            split_list.append('.')
        
        # 마지막 커서 도달 시 잔여 문자 처리 
        if cursor == len(input_str)-1 and cursor != last_dot_point:
            split_list.append(input_str[last_dot_point+1:])
            
        cursor +=1
    return split_list

def convert(split_list):
    result ='' 
    for case in split_list:
        if case[0] =='X':
            cursor = 0 
            while(cursor < len(case)):
                if len(case[cursor:]) >= 4:
                    result +='AAAA'
                    cursor +=4
                else:
                    result +='BB'
                    cursor+=2
        else:
            result+=case
    
    return result

def solution():
    #s = '...'
   # s = '..XXXX..XX.'
#    s= 'XX.XXXXXXXXXX..XXXXXXXX...XXXXXX'
    s = set_test_case()
    split_str = custom_split(s)
    if not valid_check(s):
        result = '-1'
    else:
        result = convert(split_str)
    print(result)

if __name__=='__main__':
    solution()