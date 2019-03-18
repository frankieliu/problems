
6line AC python

https://leetcode.com/problems/symmetric-tree/discuss/33068

* Lang:    python3
* Author:  so_kid
* Votes:   46




        def isSymmetric(self, root):
            def isSym(L,R):
                if not L and not R: return True
                if L and R and L.val == R.val: 
                    return isSym(L.left, R.right) and isSym(L.right, R.left)
                return False
            return isSym(root, root)
