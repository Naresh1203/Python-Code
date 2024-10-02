a=eval(input("Enter the value of x : "))
b=eval(input("Enter the value of y : "))
def f(x,y):
    z=x**2+y**2+24*x+8
    return z
result=f(a,b)
print(f"The value at {a} and {b} is {result}")
