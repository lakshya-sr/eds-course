import numpy as np

# Input matrices
print("Enter Array1:")
arr1 = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Array2:")
arr2 = np.array([list(map(int, input().split())) for i in range(3)])

# Perform horizontal stacking (hstack)
print("Horizontal Stack:\n", np.hstack((arr1,arr2)), sep="")


# Perform vertical stacking (vstack)
print("Vertical Stack:\n", np.vstack((arr1,arr2)), sep="")
