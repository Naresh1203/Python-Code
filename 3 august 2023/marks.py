a=eval(input("Enter the marks of Student Out of 100 :"))
if(a<0 or a>100):
    print("Student Marks is not in Range")
else:
    if(a>=90):
        print(f"Student got {a} marks & its Grade is O")
    elif(a>=80):
        print(f"Student got {a} marks & its Grade is A+")
    elif(a>=70):
        print(f"Student got {a} marks & its Grade is A")
    elif(a>=60):
        print(f"Student got {a} marks & its Grade is B+")
    elif(a>=50):
        print(f"Student got {a} marks & its Grade is B")
    elif(a>=40):
        print(f"Student got {a} marks & its Grade is C")
    else:
        print(f"Student got {a} marks & its Grade is F")

