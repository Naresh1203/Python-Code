from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return exp(-x**2-y**2)
ax=axes(projection='3d')
x=linspace(-2,2,500)
y=linspace(-2,2,500)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax.plot_wireframe(X,Y,Z)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title('Wireframe')
show()



