s=int(input("Enter the size of list"))
l=[]

vowel=[]
for i in range(0,s):
    le=0
    s=input("Enter the string:")
    l.append(s)
    le=len(s)-1
    if(s[le]=="a" or s[le]=="e" or s[le]=="i" or s[le]=="o" or s[le]=="u" or s[le]=="A" or s[le]=="E" or s[le]=="I" or s[le]=="O" or s[le]=="U"):
        vowel.append(s)
print(f"The list in which string whose first character is vowel is {vowel}")
