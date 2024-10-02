from sympy import *
x=eval(input("Enter the x coordinate"))
y=eval(input("Enter the y coordinate"))
p=Point(x,y)
T=[]
for i in range(0,3,1):
    l=[]
    for j in range(0,3,1):
        element=eval(input(f"Enter the element of {i+1}{j+1}th element:"))
        l.append(element)
    T.append(l)
p1=p.transform((Matrix(T)))
print(p1)
