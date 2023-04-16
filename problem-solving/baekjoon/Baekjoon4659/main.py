import sys

input = sys.stdin.readline
#https://www.acmicpc.net/problem/4659
# T = ㅇ
#     'a',
#     'tv',
#     'ptoui',
#     'bontres',
#     'zoggax',
#     'end',
#     'wiinq',
#     'eep',
#     'houctuh'
# ]

vowel = ['a','e','i','o','u']
special_characters = ['e','o']

def is_vowel(c):
    if c in vowel:
        return True
    else:
        return False

def vaild_check_case1(s):
    for v in vowel:
        if v in s:
            return True
    
    return False

def valid_check_case2(s):
    end = len(s)
    valid = True
    if end >2:
        start = 2
        while(start < end):
            if is_vowel(s[start]) and is_vowel(s[start-1]) and is_vowel(s[start-2]):
                valid = False
                break
            elif not is_vowel(s[start]) and not is_vowel(s[start-1]) and not is_vowel(s[start-2]):
                valid = False
                break
            else:
                start +=1
    return valid
def valid_check_case3(s):
    valid = True
    end = len(s)
    if end > 1:
        start = 1
        while(start < end):
            if s[start] == s[start-1]:
                if s[start] == 'o' or s[start] =='e':
                    pass
                else:
                    valid=False
                    break
            start+=1
    return valid
def is_valid_pass(s):

    if vaild_check_case1(s) and valid_check_case2(s) and valid_check_case3(s):
        return True
    else:
        return False
    


def solution():
    output_template = '<{password}> is {negative}acceptable.'
    while(True):
        s = input().replace("\n","")
        if s == 'end':
            break
        elif is_valid_pass(s):
            output = output_template.format(password=s,negative='')
        else:
            output = output_template.format(password=s,negative='not ')
        print(output)

solution()