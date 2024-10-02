s=input("Enter a string: ")
print("Reverse string is:")
for i in range(len(s)-1,-1,-1):
    print(f"{s[i]}",end="")

