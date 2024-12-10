import numpy as np
import random

# Task 1: Create a 1D array 'v' with 10 random integers between 1 and 100
v = np.array([random.randint(1, 100) for _ in range(10)])
print("Original array v:", v)

# Task 2: Create a new array with elements from odd indices of array 'v'
odd_index_values = v[1::2]
print("Values at odd indices of v:", odd_index_values)

# Task 3: Create a new array with elements of 'v' in reverse order
v_reversed = v[::-1]
print("Reversed array v:", v_reversed)

# Task 4: Predict the output of the following code:
# a = np.array([1, 2, 3, 4, 5])
# b = a[1:4]
# b[0] = 200
# print(a[1])  
# Expected output: 200 because modifying 'b' also affects 'a' as they share memory

# Task 9: Create a 5x5 2D array 'm' with random integers between 1 and 100
m = np.array([[random.randint(1, 100) for _ in range(5)] for _ in range(5)])
print("Original matrix m:\n", m)

# Task 10: Create a new array from 'm' with elements in each row reversed
m_rows_reversed = np.array([row[::-1] for row in m])
print("Matrix with each row reversed:\n", m_rows_reversed)

# Task 11: Create an array with rows of 'm' in reverse order
m_reverse_rows = m[::-1]
print("Matrix with rows in reverse order:\n", m_reverse_rows)

# Task 12: Create an array with both rows and columns of 'm' in reverse order
m_reverse_rows_columns = m[::-1, ::-1]
print("Matrix with both rows and columns reversed:\n", m_reverse_rows_columns)

# Task 13: Create a new array from 'm' by removing the outer rows and columns
m_inner = m[1:-1, 1:-1]
print("Matrix with outer rows and columns removed:\n", m_inner)
