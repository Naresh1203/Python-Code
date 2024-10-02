from matplotlib.pyplot import *
x=[25,50,15,75,12]
y=("Grocerry","Education","Car","Electricity","Loan")
pie(x,labels=y,autopct="%0.2f%%",colors=["r","g","b","c","m"],explode=[0.1,0.2,0.3,0.4,0.5],shadow="True",startangle=90)
show()

