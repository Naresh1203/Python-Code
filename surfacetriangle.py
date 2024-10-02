from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return exp(-x**2-y**2)
ax=axes(projection='3d')
x=random.uniform(low=-2,high=2,size=50)
y=random.uniform(low=-2,high=2,size=50)
z=f(x,y)
ax.plot_trisurf(x,y,z,cmap='viridis',edgecolor='Green')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title('SurfaceTriangle')
show()



