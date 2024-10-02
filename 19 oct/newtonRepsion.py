def f(x):
    y=x**2-5*x+2
    return y
def g(x):
    y=2*x-5
    return y
x0=eval(input("Enter the initial value :"))
n=int(input("Enter the number of iteration:"))
p=0
for i in range(1,n+1,1):
    if(g(x0)==0):
        print("Division by zero")
        break
    else:
        c=x0-(f(x0)/g(x0))
        print(f"x{i}={c}")
        if abs(c-p)<0.0001:
            print("Requires root is {:.4f}".format(c))
            break
        x0=c
        p=c

