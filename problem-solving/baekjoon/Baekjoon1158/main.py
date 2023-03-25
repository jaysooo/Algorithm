from collections import deque


def pretty_print(output):
    templ = "<{content}>"
    content = ""
    for i in output:
        content += str(i)+", "
    return templ.format(content=content[:-2])

def solution():
    # N = 7
    # K = 3
    input_str = input().split(" ")
    N = int(input_str[0])
    K = int(input_str[1])
    output=[]
    circle = deque([i for i in range(1,N+1)])

    cursor = K
    while(len(circle)>0):
        if cursor > 1 :
            circle.rotate(-1)
            cursor-=1
        else:
            v = circle.popleft()
            output+=[v]
            cursor = K 

    print(pretty_print(output))
    
    


solution()
    
    
    