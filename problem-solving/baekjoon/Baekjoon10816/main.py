import sys

input = sys.stdin.readline



def set_test_case():
    N = int(input())
    input_str = input().split()
    cards = [int(x) for x in input_str]
    M = int(input())
    input_str = input().split()
    your_cards = [int(x) for x in input_str]
    return cards , your_cards

def binary_search(arr,search_value):
    start = 0 
    end = len(arr)
    
    while(start<end):
        mid = (start + end) // 2
        if arr[mid] == search_value:
            return mid
        elif arr[mid] < search_value:
            start = mid+1
        else:
            end = mid
    
    return -1
        
    
   

def solution(): 
    cards,your_cards = set_test_case()
    cache = dict()
    for i in cards:
        if i not in cache:
            cache[i] = 1
        else:
            cache[i] +=1
    sorted_card = sorted(cards)
    answer = []
    for i in your_cards:
        if binary_search(sorted_card,i) > -1:
            answer += [str(cache[i])]
        else:
            answer += [str(0)]
    
    print(" ".join(answer))
    
    
            
    
            
    

solution()