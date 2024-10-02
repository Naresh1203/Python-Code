p=int(input("Enter the Number:= "))
def sumCube(n):
    sum=0
    for i in range(1,n+1,1):
        square=i**3
        sum=sum+square
    return sum
s=sumCube(p)
print(f"Sum of Cube of {p} Natural no. is {s}")


