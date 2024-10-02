l=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in range(0,len(l),1):
    if(l[i]%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])
        
print(f"List of even no. is:{even}")
print(f"List of odd no. is: {odd}")

