n=int(input("Enter the number: "))
def sum(z):
    sum=0
    for i in range(1,n+1,1):
        sum=i+sum
    return sum
s=sum(n)
print(f"The Sum of {n} natural number is {s}")
