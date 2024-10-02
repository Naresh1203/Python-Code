from matplotlib.pyplot import *
x=[80,60,35,25]
y=["20-25","25-30","30-35","35-40"]
pie(x,labels=y,autopct="%0.2f%%",colors=["y","g","r","b"],explode=[0.1,0.1,0.1,0.1],shadow=True)
legend(title="Age Group",loc="upper right")
title("PIE CHART")
show()
