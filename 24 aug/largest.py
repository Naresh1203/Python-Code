a=eval(input("Enter the first number: "))
b=eval(input("Enter the second number: "))
def smallestTwo(p,q):
    if(p>q):
        return p
    else:
        return q
m=smallestTwo(a,b)
print(f"The largest number in {a} and {b} is {m}")
