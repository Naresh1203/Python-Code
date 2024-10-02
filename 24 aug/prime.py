n=eval(input("Enter the number: "))
def prime(z):
    flag=0
    for i in range(2,n+1,1):
        if(n%i==0 and i<n):
            flag=1
    if(flag==0 and n!=1):
        print(f"{n} is Prime Number")
    else:
        print(f"{n} is not Prime Number")
prime(n)
