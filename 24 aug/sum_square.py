p=int(input("Enter the Number:= "))
def sumSquare(n):
    sum=0
    for i in range(1,n+1,1):
        square=i**2
        sum=sum+square
    return sum
s=sumSquare(p)

print(f"Sum of Square of {p} natural no. is {s}")


