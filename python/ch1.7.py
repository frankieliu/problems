# zero out column and row if element has 0
'''
..x..
xx0xx
..x..  what if there is a zero here?
..x..
'''

import numpy as np
def zero(a):
    s = a.shape
    rows = s[0]
    cols = s[1]
    zr = [False] * rows
    zc = [False] * cols
    for i in range(0, rows):
        for j in range(0, cols):
            if a[i][j] == 0:
                zr[i] = True
                zc[j] = True
    print(zr)
    print(zc)
    for i in range(0, rows):
        for j in range(0, cols):
            if zr[i] == True or zc[j] == True:
                a[i][j] = 0
    return a

a = np.array([[1,2,3],[4,0,6],[7,8,9]])
print(zero(a))
