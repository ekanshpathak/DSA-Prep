# Given n length array "arr". Find (i,j) with maximum value of arr[i] - arr[j] + j - i. 
# You need to print max value of (arr[i] - arr[j] + j - i) possible and not the (i,j) itself.

# Approach:- (arr[i] - arr[j] + j - i) - can be re-written as => (arr[i] - i) - (arr[j] - j) -> Maximize 1st entity and minimize second entity to get maximumum value of this equation
import math

n = 5
arr = [3,9,8,4,1]

largest = -math.inf
smallest = math.inf

for i in range(n):
    if arr[i] - i > largest:
        largest = arr[i] - i

    if arr[i] - i < smallest:
        smallest = arr[i] - i

print(largest - smallest)