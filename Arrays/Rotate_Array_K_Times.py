# Imp Problem => Meta, Google, Amazon, Microsoft

# Rotate the array from last to first by K times  => One rotation means Last index element will come to first index and shift all elements by 1 position

# A = [-3, 4, 2, 8, 3, 9]
# K = 3
# Output: 
# 1st Rotation:- [9, -3, 4, 2, 8, 3]
# 2nd Rotation:- [3, 9, -3, 4, 2, 8]
# 3rd Rotation:- [8, 3, 9, -3, 4, 2]

import time
A = list(range(100000000))
K = 3

# Brute Force Method => For every rotation copy last element to temp and then shift every element to one index right and then paste temp value to 1st index and repeat for K rotations
# start = time.process_time() 
# Time taken = 36 seconds
# n = len(A)
# for i in range(K):
#     temp = A[n-1]
#     for j in range(n-1, 0, -1):
#         A[j] = A[j-1]

#     A[0] = temp

# print(time.process_time() - start)
# print(A[0], A[1], A[2], A[3])

# Optimized Method 1 => Take last K elements from array and paste in starting using String methods
start = time.process_time() 
# Time Taken = 10 seconds
A = A[-K:] + A[:-K]

print(time.process_time() - start)
print(A[0], A[1], A[2], A[3])

# Optimized Method 2
# start = time.process_time() 
# Time taken = 15 seconds
# A = sorted(A, reverse=True)  # Reverse entire Array (Reverse can be done using swap method with temp varible)
# A = sorted(A[:K]) + sorted(A[K:])  # Reverse K elements and then remaining elements

# print(time.process_time() - start)
# print(A[0], A[1], A[2], A[3])
