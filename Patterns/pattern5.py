# * * * - * * *
# * * - - - * *
# * - - - - - *
# * * - - - * *
# * * * - * * *



N = 5
nsp = 1
nst = N//2 + 1

for i in range(N):
    for j in range(nst):
        print('*', end=' ')
    for k in range(nsp):
        print('-', end=' ')

    for j in range(nst):
        print('*', end=' ')

    if i <= N//2 - 1:
        nsp = nsp + 2
        nst = nst - 1
    else:
        nsp = nsp - 2
        nst = nst + 1

    print()