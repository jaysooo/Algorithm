


class Point():
    x = 0 
    y = 0 
    
    def __init__(self,x= 0, y = 0 ) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        #return f"x -> {self.x}\t y -> {self.y}"
        return f"{self.x} {self.y}"
    

def solution():
    points = []
    p4 = Point()
    for i in range(0,3):
        input_str = input().split()
        p = Point()
        p.x = int(input_str[0])
        p.y = int(input_str[1])
        #print(p)

        points +=[p]
                    
    if points[0].x == points[1].x:
        p4.x = points[2].x
        if points[2].y == max(points[0].y,points[1].y):
            p4.y = min(points[0].y,points[1].y)
        else:
            p4.y = max(points[0].y,points[1].y)
    elif points[0].x == points[2].x:
        p4.x = points[1].x
        if points[1].y == max(points[0].y,points[2].y):
            p4.y = min(points[0].y,points[2].y)
        else:
            p4.y = max(points[0].y,points[2].y)
    elif points[1].x == points[2].x:
        p4.x = points[0].x
        if points[0].y == max(points[1].y,points[2].y):
            p4.y = min(points[1].y,points[2].y)
        else:
            p4.y = max(points[1].y,points[2].y)
    else:
        pass
    print(p4)

    
    
if __name__ == '__main__':
    solution()