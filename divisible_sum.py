n=eval(input("Enter the number:"))
def summ(n):
    temp=0
    sum=0
    while(n!=0):
        temp=n%10
        n=n//10
        sum=sum+temp
    return sum
def divisible(n):
    if(n%3==0):
        print(f"{n} is divisible by 3")
divisible(summ(n))
print(f"Sum={summ(n)}")
