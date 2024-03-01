#   1
#  232
# 34543
#  232
#   1

n = 3

nsp = n//2  # No of spaces
ntp = 1  # No to Print

count = 1
for i in range(n):

    for j in range(nsp):
        print(' ', end='')
    
    ntp = count//2 + 1
    
    for k in range(count):
        print(ntp, end='')

        if k < count//2:
            ntp = ntp + 1
        else:
            ntp = ntp - 1

    if i < n//2:
        count = count + 2
        nsp  = nsp - 1

    else:
        count = count - 2
        nsp  = nsp + 1

    print()