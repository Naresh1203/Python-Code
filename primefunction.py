x=eval(input("Enter the number:"))
def prime(x):
    flag=0
    for i in range(2,x+1,1):
        if(x%i==0 and i<x):
            flag=1
            break
    if(flag==1 or x==1 or x<0):
        print(f"Given Number {x} is not prime number ")
    else:
        print(f"Given Number {x} is prime number")
prime(x)   


    
