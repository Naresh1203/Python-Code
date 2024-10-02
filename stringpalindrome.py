s=input("Enter the string:")
j=len(s)-1
flag=0
for i in range(0,len(s)//2,1):
    if(s[i]!=s[j]):
        j=j-1
        flag=1
        break
if(flag==1):
    print(f"Given string {s} is not palindrome")
else:
    print(f"Given string {s} is palindrome")


