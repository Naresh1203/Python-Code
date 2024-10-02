s=input("Enter a string: ")
for i in range(0,len(s),1):
    if(s[i]>="a" and s[i]<="z"):
        flag=1
    elif(s[i]>="A" and s[i]<="Z"):
        flag=2
    else:
        flag=0
if(flag==0):
    print(f"{s} is Not Upper case or Lower case")
elif(flag==1):
    print(f"{s} is Lower case")
elif(flag==2):
    print(f"{s} is Upper case")


