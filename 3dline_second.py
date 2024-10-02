from matplotlib.pyplot import *
from numpy import *
ax=axes(projection='3d')
z=linspace(-15,15,1000)
x=2*z
y=90*z
ax.plot(x,y,z,c='b')

ax.set_xlabel('x_axis')
ax.set_ylabel('y_axis')
ax.set_zlabel('z_axis')
ax.set_title('3D line part 2')
show()
