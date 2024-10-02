age=int(input("Enter the Age of the Person:- "))
if(age>=18):
    print(f"Age of Person is {age} and The Person is eligible for Voting")
elif(age<0):
    print(f"Person age cannot be negetive")
elif(age==0):
    print("Person age cannot be Zero")
else:
    print(f"Age of Person is {age} and The Person is Not eligible for Voting")
