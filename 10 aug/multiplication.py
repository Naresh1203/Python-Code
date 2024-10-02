n=int(input("Enter the No you want to make multiplication chart:= "))
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(i*j,end="\t")
    print()
