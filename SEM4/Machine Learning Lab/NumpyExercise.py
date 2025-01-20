# Creating a 1-D array
import numpy as np
print(np.arange(10))

# Reshaping a 1-D array
import numpy as np
l = np.arange(10).reshape(5,-1)
print(l)

# Multiply a (5,3) matrix with (3,2) matric
import numpy as np
mat1 = np.arange(0,15).reshape(5,3)
mat2 = np.arange(15,21).reshape(3,2)
result = np.dot(mat1,mat2)
print(result)

# Print odd numbers in an array
import numpy as np
l = np.array([1,3,5,3,6,7,9,5])
odd_nums = l[l%2!=0]
print(odd_nums)

# Replace all odd numbers in an array of 1-10 with -1
import numpy as np
arr = np.arange(1,11)
arr[arr%2!=0] = -1
print(arr)

# Convert a 1D array to a boolean array where all positive values become True
import numpy as np
arr = np.arange(-5,11)
arr = arr>0
print(arr)

# Replace all even numbers in a 1D array with their negative
import numpy as np
arr = np.arange(1,11)
arr[arr%2==0] = -arr[arr%2==0]
print(arr)

# Create a random 3x3 matrix and normalize it
import numpy as np
matrix = np.random.random((3,3))
print("Original Matrix\n",matrix)
normalized = (matrix - np.mean(matrix))/np.std(matrix) #Z=mat-mean/std
print("Normalized array\n",normalized)

# Calculate the sum of the diagonal elements of a 3x3 matrix
import numpy as np
matrix = np.random.random((3,3))
dsum = sum([matrix[i][i] for i in range(0,3)])
print(dsum)

# Find the indices of non-zero elements from [1,2,0,0,4,0]
import numpy as np
arr = np.array([1,2,0,0,4,0])
print(np.nonzero(arr)[0].tolist())

# Reverse a 1D array (first element becomes the last)
import numpy as np
arr = np.array([1,2,0,0,4,0])
reversed_arr = np.flip(arr)
print(reversed_arr)

# Create a 3x3 identity matrix
import numpy as np
arr = np.eye(3)
print(arr)

# Reshape a 1D array to a 2D array with 5 rows and 2 columns
import numpy as np
arr = np.random.random(10)
arr = arr.reshape(5,2)
print(arr)

# Stack two arrays vertically
import numpy as np
arr1 = np.random.random(5)
arr2 = np.random.random(5)
stack_arr = np.vstack((arr1,arr2))
print(stack_arr)

# Get the common items between two arrays
import numpy as np
arr1 = np.random.randint(0,50,size=10)
arr2 = np.random.randint(0,50,size=10)
intersect_arr = np.intersect1d(arr1,arr2)
print(intersect_arr)







