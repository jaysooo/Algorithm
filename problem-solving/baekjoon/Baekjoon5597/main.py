

def solution():
    class_room = [i for i in range(0,31)]
    for i in range(0,28):
        student = int(input())
        class_room[student] = -1
    
    results = list(filter(lambda x: x > -1, class_room))
    for i in results[1:]:
        print(i)
        
solution()