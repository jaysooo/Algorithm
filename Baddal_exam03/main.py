
def duplicatedRect(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):
    dup_rect=[]

    #not dup

    if (ax1>bx1):
        dup_rect.append(ax1)
    else:
        dup_rect.append(bx1)

    if ay1>by1:
        dup_rect.append(ay1)
    else:
        dup_rect.append(by1)

    if ax2>bx2:
        dup_rect.append(bx2)
    else:
        dup_rect.append(ax2)

    if ay2>by2:
        dup_rect.append(by2)
    else:
        dup_rect.append(ay2)

    return dup_rect

def calulateArea(rect):
    if len(rect)>=4:        
        return (rect[2]-rect[0])*(rect[3]-rect[1])
    #return (x2-x1)*(y2-y1)
    return -1

inputCase=[700 ,400 ,1600 ,1100 ,0 ,400 ,1100,900,900 ,900 ,0 ,1800 ,650]

#print(duplicatedRect(700 ,400 ,1600 ,1100 ,0 ,400 ,1100,900))
# calculate : 1 - ((1-2)+(1-3)-(2-3))
# a = (1-2) ,  b= (1-3),  c= (2-3 )
a=duplicatedRect(700 ,400 ,1600 ,1100 ,0 ,400 ,1100,900)
b=duplicatedRect(700 ,400 ,1600 ,1100, 900 ,0 ,1800 ,650)
c=duplicatedRect(0 ,400 ,1100,900, 900 ,0 ,1800 ,650)
getAnser=calulateArea(inputCase[0:4]) -(calulateArea(a)+calulateArea(b)-calulateArea(c))
print(getAnser)