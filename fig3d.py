from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return exp(-x**2-y**2)
def g(a,b):
    return a**2+2*b+3
fig=figure(figsize=(5,5))
ax=fig.add_subplot(1,2,1,projection='3d')
bx=fig.add_subplot(1,2,2,projection='3d')
x=linspace(-2,2,100)
y=linspace(-2,2,100)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax.contour3D(X,Y,Z,500)
ax.set_title('Countour 3d')

a=linspace(-2,2,100)
b=linspace(-2,2,100)
A,B=meshgrid(a,b)
C=g(A,B)
bx.contour3D(A,B,C,500)
bx.set_title('Another')
show()
