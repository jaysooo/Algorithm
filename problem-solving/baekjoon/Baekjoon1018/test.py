def test(a,b):
    print(id(a))
    return a

x=1
y=2
print(id(x))
test(x,y)