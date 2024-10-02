n=int(input("Enter the number:"))
sum=0
if(n<0):
    print("Natural number cannot be negetive or 0")
else:
    for i in range(1,n+1,1):
        print(i)
print("Square of natural number")
for i in range(1,n+1,1):
    print(i**2)
for i in range(1,n+1,1):
    sum=sum+i**3
print(f"Sum of Cube of natural number is {sum}")
