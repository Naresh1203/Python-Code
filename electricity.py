from matplotlib.pyplot import *
x=[24,14,7,5,6,4]
y=["Factories","Houses","Roads","Shops","Officies","Other"]

title=("Household Expenses")
pie(x,labels=y,autopct="%0.2f%%",colors=["r","g","b","m","y","w"],explode=[0.1,0.1,0.1,0.1,0.1,0.1],shadow=True)
legend(title="Supply of Electricity",loc="upper right")
show()

