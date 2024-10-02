s=input("Enter the string:")
lower=False
Upper=False
for i in range (0,len(s),1):

    if("a"<=s[i]>="z"):
        lower=True
    elif("A"<=s[i]>="Z"):
        Upper=True
    else:
        print(f"invalid")
        break
if(lower==True and Upper==True):
    print("string {s} is mix up of Lower and Upper")
elif(lower==True):
    print("String {s} is in Lower case")
else:
    print("String is in Upper Case.")    