import numpy as np

rows, columns = (int(i) for i in input().split())
arr = np.empty((rows,columns), dtype=int)
arr.reshape((rows,columns))
for i in range(rows):
	data = [int(x) for x in input().split()]
	for j in range(columns):
		arr[i][j] = data[j]

print(arr)
print(arr.ndim)
print(np.shape(arr))
print(rows*columns)
