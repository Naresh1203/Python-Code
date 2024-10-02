n=int(input("Enter the number you want to make multiplication chart:"))
j=1
while(j<=n):
    for i in range(1,11,1):
        print(f"{i*j}")
    j=j+1
    print(end="\t")


