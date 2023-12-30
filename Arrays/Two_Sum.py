# Find Pair(i,j) such that arr[i]+arr[j]==K and i != j

A = [2, -1, 0, 3, 2, 5, 7]
K=4

n = len(A)

for i in range(n-1):
    rem = K-A[i]
    for j in range(i+1,n):
        if A[j] == rem:
            print(f'({i}, {j})')