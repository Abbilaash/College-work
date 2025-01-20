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

# Create a 5x5 matrix with row values ranging from 0 to 4
import numpy as np
matrix = np.zeros((5,5))
matrix += np.arange(5)
print(matrix)

# Find the index of the maximum value in a 1D array
import numpy as np
arr = np.random.random(10)
print(arr)
print("Index:",np.argmax(arr)," Value:",arr[np.argmax(arr)])

# Normalize the values in a 1D array between 0 and 1.
import numpy as np
arr = np.array([2,3,5,6,17,20])
normalized_arr = (arr - np.min(arr))/(np.max(arr) - np.min(arr))
print(normalized_arr)

# Calculate the dot product of two arrays
import numpy as np
arr1 = np.random.randint(10,20,size=5)
arr2 = np.random.randint(0,10,size=5)
print(np.dot(arr1,arr2))

# Count the number of elements in an array within a specific range (20 to 30)
import numpy as np
arr = np.random.randint(10,50,size=20)
count = np.sum((arr>=20) & (arr<=30))
print(arr)
print(count)

# Find the mean of each row in a 2D array
import numpy as np
arr = np.random.randint(10,50,(3,3))
print(arr)
print(np.mean(arr,axis=1))

# Create a random 4x4 matrix and extract the diagonal elements
import numpy as np
matrix = np.random.randint(10,50,(4,4))
print(matrix)
print(np.diag(matrix))

# Count the number of occurrences of a specific value in an array (n=15)
import numpy as np
arr = np.random.randint(10,20,size=20)
count = np.count_nonzero(arr==15)
print(arr)
print(count)

# Replace all values in a 1D array with the mean of the array
import numpy as np
arr = np.random.randint(10,50,size=10)
print(arr)
mean = np.mean(arr)
arr[:] = mean
print(arr)

# Find the indices of the maximum and minimum values in a 1D array
import numpy as np
arr = np.random.randint(10,50,size=10)
print(arr)
print("Minimum ind: ",np.argmin(arr))
print("Maximum ind: ",np.argmax(arr))

# Create a 2D array with 1 on the border and 0 inside
import numpy as np
matrix = np.ones((5,5))
matrix[1:-1,1:-1] = 0
print(matrix)

# Find the unique values and their counts in a 1D array
import numpy as np
arr = np.random.randint(0,15,size=20)
values, counts = np.unique(arr, return_counts=True)
print("Unique:", values)
print("Counts:", counts)




















