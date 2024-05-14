#  Given N 2D Points, Calculate no. of distinct points among them.

# Ex: x[5] = {2, 1, 3, 2, 2}
#     y[5] = {3, 1, 2, 3, 4}
    
# The first array represents the x co-ordinates, the second array represents the y co-ordinate. Acoording to above examples the points are 
#     (x[0],y[0])->(2,3)
#     (x[1],y[1])->(1,1)
#     (x[2],y[2])->(3,2)
#     (x[3],y[3])->(2,3)
#     (x[4],y[4])->(2,4)
    
# Total number of distinct points are 4.

n = 5
x = [2, 1, 3, 2, 2]
y = [3, 1, 2, 3, 4]

hs = set()  # As Set does not contain duplicate values, so it will only keep distinct coordinates

for i in range(n):
    tup = (x[i], y[i])
    hs.add(tup)

print(hs)
print(len(hs))