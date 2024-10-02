n=eval(input("Enter the number: "))
def arm(n):
    power=n
    num=n
    i=0
    temp=0
    sum=0
    while(power!=0):
        i=i+1
        power=power//10
    while(n!=0):
        temp=n%10
        sum=sum+temp**i
        n=n//10
    if(num==sum):
        print(f"Given number {num} is armstrong number")
    else:
        print(f"Given number {num} is not armstrong number")
arm(n)