

def solution():
    ABC = []
    number = [0] * 10
    for i in range(0,3):
        ABC += [int(input())]
        
    multiply = ABC[0]* ABC[1] * ABC[2] 
    for n in str(multiply):
        number[int(n)] +=1
    
    for i in number:
        print(i)
        

solution()