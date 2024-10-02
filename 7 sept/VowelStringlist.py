l=[]
vowel=[]
n=int(input("Enter the size of List: "))
for i in range(0,n,1):
    string=input(f"Enter the {i+1}th string: ")
    l.append(string)
    if(string[0]=="a" or string[0]=="e" or string[0]=="i" or string[0]=="o" or 		string[0]=="u" or string[0]=="A" or string[0]=="E" or string[0]=="I" or string[0]=="O" or string[0]=="U"):
        vowel.append(string)
print(f"The list whose first character is stat with vowel : {vowel}") 
