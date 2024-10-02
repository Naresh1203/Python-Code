l=[]
vowel=[]
n=int(input("Enter the size of List: "))
for i in range(0,n,1):
    string=input(f"Enter the {i+1}th string: ")
    le=len(string)-1
    l.append(string)
    if(string[le]=="a" or string[le]=="e" or string[le]=="i" or string[le-1]=="o" or string[le]=="u" or string[le]=="A" or string[le]=="E" or string[le]=="I" or string[le]=="O" or string[le]=="U"):
         vowel.append(string)
print(f"The string whose end letter is vowel in list is: {vowel}") 
