import sys
input = sys.stdin.readline

def set_test_case():
    command_line = int(input())
    commands=[]
    for i in range(0,command_line):
        commands+=[input()]

    return commands

def move_turtle(location,direction,move):
    # location[0] -> X 축 location[1] -> Y 축
    if direction ==3 or direction ==2:
        move = move * -1
        
    if direction == 0 or direction ==2:
        location[1] = location[1] + move
    elif direction == 1 or direction == 3:
        location[0] = location[0] + move
    else:
        pass

    return location

def move_direction(current, direction):
    # 0 : up , 1 : right , 2 : down , 3: left
    if direction == 'R':
        current = (current+1)%4
    elif direction == 'L':
        current = (current-1)%4
    else:
        pass
    return current

def solution():
    commands = set_test_case()
    
    for command in commands:
        turtle_direction = 0 # default direction -> UP
        turtle_location=[0,0] # default location
        maximum_location=[0,0,0,0] # UP , RIGHT, DOWN, LEFT 
        
        for c in command:

            # set location by command
            if c == 'L' or c=='R':
                turtle_direction = move_direction(turtle_direction,c)
            elif c == 'F':
                turtle_location = move_turtle(turtle_location,turtle_direction,1)
            elif c == 'B':
                turtle_location = move_turtle(turtle_location,turtle_direction,-1)
            
           # save maximum location of turtle  
            if c == 'F' or c == 'B':
                if turtle_location[0] > maximum_location[1]:
                    maximum_location[1]=turtle_location[0]                    
                    
                elif turtle_location[1] > maximum_location[0]:
                    maximum_location[0]=turtle_location[1]
                    
                elif turtle_location[0] < maximum_location[3]:
                    maximum_location[3] = turtle_location[0]
                
                elif turtle_location[1] < maximum_location[2]:
                    maximum_location[2] = turtle_location[1]
            
        # result print
        if (maximum_location[1] == 0 and maximum_location[3] ==0) or (maximum_location[0] == 0 and maximum_location[2] ==0): 
            print(0)
        else:
            print((abs(maximum_location[0])+abs(maximum_location[2])) * (abs(maximum_location[1])+abs(maximum_location[3])))
            

if __name__=='__main__':
    solution()
    