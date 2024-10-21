import numpy as np

A = np.linspace(1,24,12)
A = np.round(A)
print(f"Array A: {A}")

array_b = A.reshape(3,4)
print(f"\nSize 3x4 Array B: \n{array_b}")