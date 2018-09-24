# rotate +90
'''
x will go to y

 .x...
 .   w
 .   .
 y   .
 ...z.

For x->y: index [0,1]       -> [n-2,0]
For w->x: index [1,n-1]     -> [0,1]
For z->w: index [n-1,n-2]   -> [1,n-1]
For y->z: index [n-2,0]     -> [n-1,n-2]

Shifting to a different position:

For x->y: index [0,i]       -> [n-1-i,0]
For w->x: index [i,n-1]     -> [0,i]
For z->w: index [n-1,n-1-i] -> [i,n-1]
For y->z: index [n-1-i,0]   -> [n-1,n-i-1]

Shifting to a middle layer:
m = 1
  i
.......
 .x...   row: m,i      x: (m, i)
 .   w                 w: (i, n-1-m)
 .   .
 y   .                 y: (n-1-i, m)
 ...z.   row: n-1-m    z: (n-1-m, n-1-i)
.......
 col
 m   n-1-m

For x->y: index [m,i]           -> [n-1-i,m]     OK
For w->x: index [i,n-1-m]       -> [m,i]         OK
For z->w: index [n-1-m,n-1-i]   -> [i,n-1-m]     OK
For y->z: index [n-1-i,m]       -> [n-1-m,n-1-i] OK


'''
import math
import numpy as np

def rotate(a):
    n = a.shape[0]
    for m in range(0, math.floor(n/2)):
        for i in range(m, n-1-m):   # picks the correct columns ind of m
            tmp = a[n-1-i][m]
            a[n-1-i][m] = a[m][i]
            a[m][i] = a[i][n-1-m]
            a[i][n-1-m] = a[n-1-m][n-1-i]
            a[n-1-m][n-1-i] = tmp
            '''
            print("m {} i {}".format(m,i))
            print("[{}][{}] <- [{}][{}]".format(n-1-i,m,m,i))
            print("[{}][{}] <- [{}][{}]".format(m,i,i,n-1-m))
            print("[{}][{}] <- [{}][{}]".format(i,n-1-m,n-1-m,n-1-i))
            print("[{}][{}] <- [{}][{}]".format(n-1-m,n-1-i,n-1-i,m))

            m 0 i 0
            [1][0] <- [0][0]   correct
            [0][0] <- [0][1]   correct
            [0][1] <- [1][1]   correct
            [1][1] <- [1][0]   correct
            m 0 i 1
            [0][0] <- [0][1]
            [0][1] <- [1][1]
            [1][1] <- [1][0]
            [1][0] <- [0][0]
            [[4 3]
             [2 1]]

            '''
            '''
            For x->y: index [m,i]           -> [n-1-i,m]
            For w->x: index [i,n-1-m]       -> [m,i]
            For z->w: index [n-1-m,n-1-i]   -> [i,n-1-m]
            For y->z: index [n-1-i,m]       -> [n-1-m,n-1-i]
            '''
    return a

# a = np.array([[1,2],[3,4]])
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],np.int32)


if False:
    n = a.shape[0]
    for i in range(0, n):
        for j in range(0, n):
            print(a[i][j])
print(a)
rotate(a)
print(a)
