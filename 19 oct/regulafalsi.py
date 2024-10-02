def f(x):
    y=x**2-5*x+2
    return y
a=eval(input("Enter the initial value :"))
b=eval(input("Enter the second value :"))
if(f(a)*f(b)>0):
    print(f"Value of {a} and {b} wrong taken")
    
else:
    print(f" a={a} and b={b}")
    n=int(input("Enter the number of iteration:"))
    p=0
    for i in range(1,n+1,1):
        if(a==b):
            print("False interval")
            break
        else:
            c=(a*f(b)-b*f(a))/(f(b)-f(a))
            print(f"x{i}={c}")
            if f(c)*f(a)<0:
                print(f"Root lies between {a} and {c}")
                b=c
            else:
                a=c
        
        if(abs(f(c)-f(p))<0.0001):
            print("Required root is {:.4f}".format(c))
            break
        p=c


    

