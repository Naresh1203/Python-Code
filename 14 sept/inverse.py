import numpy as np

m = int(input("Enter how many rows you want: "))
n = int(input("Enter how many columns you want: "))
A = []

for i in range(m):
    l = []
    for j in range(n):
        element = float(input(f"Enter the {i+1}{j+1}th element: "))  # Adjusted indexing
        l.append(element)
    A.append(l)

print("Matrix A:")
print(np.array(A))

try:
    inverse = np.linalg.inv(A)
    print(f"Inverse of Matrix A is:")
    print(inverse)
except np.linalg.LinAlgError:
    print(f"Inverse of Matrix A does not exist")
