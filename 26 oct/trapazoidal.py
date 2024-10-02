def f(x):
    y=1/(1-x+x**2)
    return y
a=int(input("Enter the lower limit of function:"))
b=int(input("Enter the upper limit of function:"))
n=int(input("Enter how many itteretion you want:"))
h=(b-a)/n
term1=0
term2=0
term1=f(a)+f(b)
for i in range (1,n,1):
    c=a+(i*h)
    term2=term2+f(c)
result=h/2*(term1+2*term2)
print("The output of given function using trapazoidal rule is {:.4f}".format(result))

