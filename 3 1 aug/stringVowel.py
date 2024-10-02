s=input("My string is : ")
vowel=0
for i in range(0,len(s),1):
    if(s[i]=='a'or s[i]=='e'or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
        if(s.count(s[i])>1):
       		count=1;
            vowel=count+1
            print(s[i])
print(f"There are {vowel} vowel in {s}")
    
