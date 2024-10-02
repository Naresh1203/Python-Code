n=eval(input("Enter the number:"))
if(n%3==0 and n%5==0 and n%7==0 ):
    print(f"{n} is divisble by 3,5,7")
elif(n%3==0 and n%5==0):
    print(f"{n} is divisible by 3,5")
elif(n%5==0 and n%7==0):
    print(f"{n} is divisible by 5,7")
elif(n%3==0 and n%7==0):
    print(f"{n} is divisible by 3,7")
elif(n%3==0):
    print(f"{n} is divisible by 3")
elif(n%5==0):
    print(f"{n} is divisible by 5")
elif(n%7==0):
    print(f"{n} is divisible by 7")
else:
    print(f"{n} is not divisible by 3,5,7")
