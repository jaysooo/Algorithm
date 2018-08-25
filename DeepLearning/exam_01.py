import numpy as np

def AND2(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(x*w)+b
    if tmp < 1:
        return 0
    else:
        return 1
    print(tmp)

def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y

def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.3
    tmp=np.sum(w*x)+b

    if tmp > 0.1:
           
        return 0

def AND(x1,x2):
    w=[0.4,0.4]
    theta=0.5
    tmp=w[0]*x1+w[1]*x2
    if theta > tmp:
        return 0 
    elif theta < tmp:
        return 1

def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=+1
    tmp=np.sum(w*x)+b
    if tmp > 0:
        return 1
    else:
        return 0

#AND2(0,1)
#print(AND(0,0))
print(XOR(1,0))

