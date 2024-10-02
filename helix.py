from matplotlib.pyplot import *
from numpy import *
ax=axes(projection='3d')
z=linspace(-15,15,1000)
x=sin(z)
y=cos(z)
ax.plot(x,y,z,c='b')

ax.set_xlabel('x_axis',c='r')
ax.set_ylabel('y_axis',c='b')
ax.set_zlabel('z_axis',c='g')
ax.set_title('Helix')
show()
