from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return y-x
def g(x,y):
    return sin(x*y)
def h(x,y):
    return x+y
def i(x,y):
    return 2*x+3*y
def j(x,y):
    return x**2+y**2
    
fig=figure(figsize=(5,5))
ax=fig.add_subplot(3,3,1,projection='3d')
bx=fig.add_subplot(3,3,2,projection='3d')
cx=fig.add_subplot(3,3,3,projection='3d')
dx=fig.add_subplot(3,3,4,projection='3d')
ex=fig.add_subplot(3,3,5,projection='3d')

x=linspace(-2,2,100)
y=linspace(-2,2,100)
X,Y=meshgrid(x,y)

Z=f(X,Y)
ax.contour3D(X,Y,Z,500)
ax.set_title('Countour 3d for y-x')
X,Y=meshgrid(x,y)

Z=g(X,Y)
bx.contour3D(X,Y,Z,500)
bx.set_title('Another')

Z=h(X,Y)
cx.plot_wireframe(X,Y,Z)
cx.set_title('Wireframe')

Z=i(X,Y)
dx.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='viridis',edgecolor='Green')


a=random.uniform(low=-2,high=2,size=50)
b=random.uniform(low=-2,high=2,size=50)
c=j(a,b)

ex.plot_trisurf(a,b,c,cmap="viridis")

show()






show()

