n=int(input("Enter the number"))
def natural(n):
    if(n<0):
        print("Natural number cannot be negetive.")
        exit()
    sum=0
    for i in range(1,n+1,1):
        sum=sum+i;
    return sum
result=natural(n)
print(f"Result: sum={result}")

