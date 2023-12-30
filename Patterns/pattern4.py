#   *
#  ***
# *****
#  ***
#   *


N = 5
nst = 1
nsp = N//2

for i in range(N):
    for j in range(nsp):
        print(' ', end=' ')
    for k in range(nst):
        print('*', end=' ')
    
    if i <= N//2-1:
        nst = nst + 2
        nsp = nsp - 1
    else:
        nst = nst - 2
        nsp = nsp + 1
    
    print()
