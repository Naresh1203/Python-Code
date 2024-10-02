import math
s=int(input("Enter the Size of list:"))

l=[] ##list define
perfect=[] ## perfect square list define
print("Enter the element.")
for i in range(0,s):
    element=int(input())
    l.append(element)
for i in range(0,s):
    if (math.sqrt(l[i]) .is_integer()):
        perfect.append(l[i])
print("Perfect square list is ")
        
print(perfect)


