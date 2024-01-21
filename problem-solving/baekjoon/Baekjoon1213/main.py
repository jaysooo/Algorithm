from collections import OrderedDict



def solution():
    input_str = input()
    name_length = len(input_str)
    gift_name = [''] * name_length

    ordered_str = sorted(input_str)
    dic = OrderedDict()

    for s in ordered_str:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1 

    # 팰린드롬 가능 체크  = v -  홀수 1개 && 모든 수의 짝수 / 모든 짝수
    mid_char = '_'
    char_set = []
    cursor = 0 
    for k, v in dic.items():    
        # print(f"k : {k} v : {v}")
        char_set += [k]
        if (v % 2 != 0) : # 홀수
            if mid_char == '_':
                mid_char = k
            else:
                print("I'm Sorry Hansoo")
                return 
    
    for i in range(0,name_length//2):
        if dic[char_set[cursor]] < 2 :
            cursor +=1    
        gift_name[i] = char_set[cursor]
        end_pos = -1 if i == 0 else (i * -1) -1
        gift_name[end_pos] = char_set[cursor]
        dic[char_set[cursor]] -= 2
        
        if dic[char_set[cursor]] < 2 :
            cursor +=1
    if name_length % 2 > 0 :
        gift_name[len(gift_name)//2]= mid_char        
    print("".join(gift_name))


if __name__=="__main__" :
    solution()

