import math
l=[]
perfect=[]
num=[]
n=int(input("Enter the size of list: "))
for i in range(0,n,1):
    element=int(input(f"Enter {i+1}th element in list: "))
    l.append(element)
maximum=max(l)
for i in range(1,maximum,1):
    num.append(i)
for i in range(0,n,1):
    sqrt_num=math.sqrt(l[i])
    if sqrt_num. is_integer():
        perfect.append(l[i])
print(f"Original list :{l}")
print(f"Original perfect square list is :{perfect}")

