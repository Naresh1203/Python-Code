from matplotlib.pyplot import *
from numpy import *
ax=axes(projection='3d')
z=linspace(-15,15,1000)
x=z
y=z
ax.plot(x,y,z,c='b')

ax.set_xlabel('x_axis',c='y')
ax.set_ylabel('y_axis',c='r')
ax.set_zlabel('z_axis')
ax.set_title('3D line')
show()
