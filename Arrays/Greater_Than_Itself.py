# Problem:- Count Total no of elements having atleast 1 element greater than itself

import time
import random

A = [-4,-3, 7, 9, 3, 9, 4, 3]
total = 0
a_dict = {}
n = len(A)
# Brute Forece Method => Pick every element and compare with all other elements
# start = time.process_time() 

# for i in range(n):
#     for j in A:
#         if A[i] < j:
#             total = total + 1
#             break

# print(time.process_time() - start)
# print(total)

# Optimized Method 1 => Using Dictionary will give you distinct element count
# start = time.process_time() 

# for i in range(n):
#     if A[i] in a_dict:
#         a_dict[A[i]] = a_dict[A[i]] + 1
#     else:
#         a_dict[A[i]] = 1

# a_dict = dict(sorted(a_dict.items()))
# print(a_dict)
# total = len(a_dict)-1

# print(time.process_time() - start)
# print(total)


# Optimized Method 2 => Using Max element -> First find which is max element in the array and then find its total occurence, final output = (Total length - Max occurence)

start = time.process_time() 

max = A[0]
max_count = 0
for i in range(1, n):
    if A[i] > max:
        max = A[i]

for i in range(n):
    if A[i] == max:
        max_count = max_count + 1

total = n-max_count

print(time.process_time() - start)
print(total)