n=eval(input("Enter the Number:"))
last=n%10
if(last%3==0):
    print(f"{last} is divisible by 3")
else:
    print(f"{last} is not divisible by 3")
