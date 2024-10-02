from numpy import *
from bezier import *
from matplotlib.pyplot import *
l1=[]
l2=[]
n=int(input("Enter the length of column:"))
for i in range(0,n,1):
    num=eval(input("Enter the point"))
    l1.append(num)
print("\n")
for i in range(0,n,1):
    num=eval(input("Enter the point"))
    l2.append(num)

t=eval(input("Enter the value of t:"))
node =asfortranarray([l1,l2])
curve=Curve.from_nodes(node)
print(curve)
point=curve.evaluate(t)
print(point)
ax=curve.plot(num_pts=100)
show()

