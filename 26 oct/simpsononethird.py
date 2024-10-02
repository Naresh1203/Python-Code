def f(x):
    y=1/(1-x+x**2)
    return y
a=int(input("Enter the lower limit of function:"))
b=int(input("Enter the upper limit of function:"))
n=int(input("Enter how many itteretion you want:"))
h=(b-a)/n
term1=0
term2=0
c=0
term1=f(a)+f(b)
for i in range(1,n):
    c=a+(i*h)
    if(i%2==0):
        term2+=2*f(c)
    else:
        term2+=4*f(c)
result=h/3*(term1+term2)
print("The output of simpsons 1/3rule is {:.4f}".format(result))

