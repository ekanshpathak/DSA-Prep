A = [1,2,3,4]

for start in range(len(A)):
    for end in range(start, len(A)):
        for i in range(start, end+1):
            print(A[i], end=' ')

        print('')
