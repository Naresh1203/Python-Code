s=int(input("Enter the size of list"))
l=[]
vowel=[]
for i in range(0,s):
    s=input("Enter the string:")
    l.append(s)
    if(s[0]=="a" or s[0]=="e" or s[0]=="i" or s[0]=="o" or s[0]=="u" or s[0]=="A" or s[0]=="E" or s[0]=="I" or s[0]=="O" or s[0]=="U"):
        vowel.append(s)
print(f"The list in which string whose first character is vowel is {vowel}")
