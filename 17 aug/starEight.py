n=int(input("Enter the number:- "))
for i in range(n,0,-1):
    print(" " * (n-i)+"* " * i )
for i in range(1,n+1,1):
    print(" " * (n-i)+"* " * i)
    