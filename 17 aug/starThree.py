n=int(input("Enter the Number:- "))
for i in range(1,n+1,1):
    for j in range(n-i,0,-1):
        print(end=" ")
    star=i * "*"
    print(f"{star}")
    print("\n")
    
