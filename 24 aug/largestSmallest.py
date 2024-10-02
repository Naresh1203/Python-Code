a=eval(input("Enter the first number: "))
b=eval(input("Enter the second number: "))
def smallestTwo(p,q):
    if(p<q):
        print(f"The largest number is {q} \n The Smallest number is {p}")

    else:
        print(f"The largest number is {p} \nThe Smallest number is {q}")
smallestTwo(a,b)

