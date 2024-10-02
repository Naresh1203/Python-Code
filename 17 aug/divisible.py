number=eval(input("Enter the Number:- "))
if(number%3==0):
    print(f"The Number {number} is divisible by 3")
else:
    print(f"The Number {number} is not divisible by 3")
if(number%5==0):
    print(f"The Number {number} is divisible by 5")
else:
    print(f"The Number {number} is not divisible by 5")
if(number%7==0):
    print(f"The Number {number} is divisible by 7")
else:
    print(f"The Number {number} is not divisible by 7")
if(number%3==0 and number%5==0):
    print(f"The Number {number} is divisible by 3 and 5")
else:
    print(f"The Number {number} is not divisible by 3 and 5")
if(number%5==0 and number%7==0):
    print(f"The Number {number} is divisible by 5 and 7")
else:
    print(f"The Number {number} is not divisible by 5 and 7")
if(number%3==0 and number%7==0):
    print(f"The Number {number} is divisible by 3 and 7")
else:
    print(f"The Number {number} is not divisible by 3 and 7")
if(number%3==0 and number%7==0 and number%5==0):
    print(f"The Number {number} is divisible by 3,5 and 7")
else:
    print(f"The Number {number} is not divisible by 3,5 and 7")
    
