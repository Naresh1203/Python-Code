##Write a program to accept a matrix from user of order nXn and check wheher it is diagonlizable or not if it is diagonalizable find matrix P,D.




from sympy import *
r=int(input("Enter the square matrix of order:"))
c=r
A=[]
for i in range(0,r,1):
    l=[]
    for j in range(0,c,1):
        element=eval(input(f"Enter the element of {i+1}{j+1}th element:"))
        l.append(element)
    A.append(l)
print(f"User Matrix is")
print(Matrix(A))

if(Matrix(A).is_diagonalizable()==True):
    P,D=(Matrix(A)).diagonalize()
    print("Given Matrix is diagonalizable")
    print(f"P={P}")
    print(f"D={D}")
else:
    print("Given Matrix is not diagonalizable ")
           


