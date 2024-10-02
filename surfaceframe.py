from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return exp(-x**2-y**2)
ax=axes(projection='3d')
x=linspace(-2,2,50)
y=linspace(-2,2,50)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='viridis',edgecolor='Green')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title('Surface')
show()



