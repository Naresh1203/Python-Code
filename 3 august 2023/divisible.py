a=eval(input("Enter a Number :"))
if(a%3==0):
    print(f"{a} is divisible by 3")
if(a%5==0):
    print(f"{a} is divisible by 5")

if(a%3==0 and a%5==0):
    print(f"{a} is divisible by both 3 & 5")
else:
    print(f"{a} is not divisible by 3,5")


