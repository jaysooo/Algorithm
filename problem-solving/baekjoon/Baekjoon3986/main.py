
def input_test_case():
    N = int(input())
    words = []
    for i in range(0,N):
        words += [input()]
        
    return words

def check_good_word(word):
    stack = []
    pre_char_idx = -1

    for c in word :
        if pre_char_idx >=0 and stack[pre_char_idx] == c :
            stack.pop()
            pre_char_idx -=1
        else:
            stack.append(c)
            pre_char_idx+=1
        
    return True if len(stack) == 0 else False
    

def solution():
    words = input_test_case()
    count = 0 
    for w in words:
        if check_good_word(w):
            count+=1
            
    print(count)       
    
solution()
