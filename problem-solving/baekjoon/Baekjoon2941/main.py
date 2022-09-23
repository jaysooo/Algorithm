

croatia_dict = {
    "c=" : 1,
    "c-" : 2,
    "dz=" : 3,
    "d-" : 4,
    "lj" : 5,
    "nj" : 6,
    "s=" : 7,
    "z=" : 8
}

def solution():
    word = input()
    #word = 'ljes=njak'
    offset = 0
    end = len(word)
    count = 0 
    
    while(offset < end):
        if (offset + 3)  <= end and word[offset:offset+3] == 'dz=':
            count +=1
            offset +=3
        elif (offset + 2) <= end and word[offset:offset+2] in croatia_dict:
            count +=1
            offset +=2
        else:
            count +=1
            offset +=1
    
    print(count)
            
solution()