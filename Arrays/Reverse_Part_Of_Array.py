# A = [-3, 4, 2, 8, 3, 9, 6, 2, 8, 10]
# {S,E} = [3,7]  //  Start & End Points for reverse
# output = [-3 4 5 2 6 9 3 8 8 10]


A = [-3, 4, 2, 8, 3, 9, 6, 2, 8, 10]
B = A.copy()
s, e = 3, 7

def swap(s, e):
    temp = A[s]
    A[s] = A[e]
    A[e] = temp
    
while s < e:
    swap(s, e)
    s = s+1
    e = e-1

print(B)
print(A)


# Advanced Question Modification:- len(Array) = n, Rotations = K and n < K

# if n=4, K=100 => A = [4, 1, 6, 9] => After 4 rotations => [4, 1, 6, 9] => You will get same array, 
# So (K % n) = (100 % 4) = 0 => 
# If you get mod = 0, you will get same array
# Otherwise, if mod != 0, then rorate the Array (mod) times => with any method mentioned above
