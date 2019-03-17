
Python - 32 ms only ! 100% faster #codegirl

https://leetcode.com/problems/flipping-an-image/discuss/242412

* Lang:    python3
* Author:  lshirursudhakar
* Votes:   0

```
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #reverse each list 
        row=len(A)
        col=len(A[0])
        B=[]
        c=[]
        for i in range(row):
            B=A[i]
            B.reverse()
            c.append(B)
        for i in range(row):
            for j in range(col):
                if(c[i][j]==1):
                    c[i][j]=0
                else:
                    c[i][j]=1
        return c
        
```
