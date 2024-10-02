l=[]
even=[]
odd=[]
n=int(input("Enter the No. you want to insert in list:"))
for i in range (0,n,1):
    num=int(input(f"Enter the {i+1}th no.:"))
    l.append(num)
for i in range(0,n,1):
    if(l[i]%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])
print(f"Even list is {even} and odd list is {odd}")

    