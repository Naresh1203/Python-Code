x=eval(input("Enter the first Number:"))
y=eval(input("Enter the second number:"))
z=eval(input("Enter the third number:"))
def fun(x,y,z):
    if(x<y and x<z):
        if(y<z):
            print(f"{x} is smallest no and {z} is largest no")
        else:
            print(f"{x} is smallest no. and {y} is largest no")
    elif(y<x and y<z):
        if(x<z):
            print(f"{y} is smallest no. and {z} is largest no")
        else:
            print(f"{y} is smallest no. and {x} is largest no")
    elif(z<x and z<y):
        if(x<y):
            print(f"{z} is smallest no. and {y} is largest no")
        else:
            print(f"{z} is smallest no. and {x} is largest no")
    else:
        print(f"{x} and {y} and {z} are same")
fun(x,y,z)

