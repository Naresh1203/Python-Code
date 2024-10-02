a=eval(input("Enter the first number:"))
b=eval(input("Enter the second number:"))

print("Enter 1 for Addition\nEnter 2 for Substraction \nEnter 3 for Multiplication\nEnter 4 for Division\nEnter 5 for Interger Division \nEnter 6 for Power")
choise=int(input("Enter your Choise:"))
if(choise==1):
    print(f"Addition of {a}+{b} is {a+b}")
elif(choise==2):
    print(f"Subtraction of {a}-{b} is {a-b}")
elif(choise==3):
    print(f"Multiplication of {a}*{b} is {a*b}")
elif(choise==4):
    print(f"Division of {a}/{b} is {a/b}")
elif(choise==5):
    print(f"Integer Division of {a}//{b} is {a//b}")
elif(choise==6):
    print(f"Power of {a}^{b} is {a**b}")
