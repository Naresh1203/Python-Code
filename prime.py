n=eval(input("Enter the Number: "))
flag=0
for i in range(2,n+1,1):
    if(n%i==0 and i<n):
        flag=1
if(n<1):
    print(f"Number should be positive")
elif(n==1):
    print(f"{n} is not a prime number")
elif(flag==1):
    print(f"{n} is not a prime number ")
else:
    print(f"{n} is prime number")
