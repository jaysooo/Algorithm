
def self_number_by_str(n):
    str_n = str(n)
    digit_sum = 0 
    for c in str_n:
        digit_sum += int(c)
    return n + digit_sum
    
def self_number():
    tmp  = set()
    self_number_set = set()
    for i in range(1,10000):
        tmp.add(i)
    i = 1
    #print(tmp)
    while(True):
        self_number = self_number_by_str(i)
        if self_number >= 15000:
            break
        self_number_set.add(self_number)
        if self_number in tmp:
            tmp.remove(self_number)
        i +=1
    
    # print('---------------')
    for i in tmp:
        print(i)

        
self_number()
