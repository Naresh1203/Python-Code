n=eval(input("Enter the number :"))
flag=0
for i in range(2,n+1,1):
    if(n%i==0 and i<n):
        flag=1
        break
if(flag==1 or n==1 or n<0):
    print(f"Given number is not prime number.")
else:
    print(f"Given number is prime number.")

