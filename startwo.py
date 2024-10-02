n=int(input("Enter the number :"))
last=0
j=0
for i in range(n,0,-1):
    last=j*" "+(i*" *")
    j=j+1
    print(last)
j=1
for i in range(n-1,-1,-1):
    last=i*" "+(j*" *")
    j=j+1
    print(last)
