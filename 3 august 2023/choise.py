a=eval(input("Enter First Number :"))
b=eval(input("Enter Second Number :"))
print("For Addition Enter : 1")
print("For Subtraction Enter : 2")
print("For Multiplication Enter : 3")
print("For Division Enter : 4")
print("For Power Enter : 5")
print("For Int Division Enter : 6")
choise=int(input("Enter Your Arthmetic Operation :"))
if(choise==1):
    print(f"Addition of {a} and {b} is :{a+b}")
elif(choise==2):
    print(f"Subtraction of {a} and {b} is :{a-b}")
elif(choise==3):
    print(f"Multiplication of {a} and {b} is :{a*b}")
elif(choise==4):
    print(f"Division of {a} and {b} is :{a/b}")
elif(choise==5):
    print(f"Power of {a}^{b} is :{a**b}")
elif(choise==6):
    print(f"Integer Division of {a} and {b} is :{a//b}")
else:
    print("The Number you enter is not in Range")
