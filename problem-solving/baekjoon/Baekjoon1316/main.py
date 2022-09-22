

from posixpath import abspath

def is_group_word(word):
    distinct_char = set()
    for c in word:
        distinct_char.add(c)
    
    temp =[]
    offset = 0 
    while(offset < len(word)):
        if offset == len(word)-1:
            temp += [word[offset]]

        elif word[offset] != word[offset+1]:
            temp += [word[offset]]
        
        offset +=1
    if len(distinct_char) != len(temp):
        return False
    else:
        return True
        

def solution():
    N = int(input())
    count = 0
    for i in range(0,N):
        word = input()
        if is_group_word(word):
            count +=1
        
    print(count)

solution()