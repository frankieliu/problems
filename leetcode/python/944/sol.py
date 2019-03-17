
Python 128 ms

https://leetcode.com/problems/delete-columns-to-make-sorted/discuss/240225

* Lang:    python3
* Author:  dacheng0413
* Votes:   1

```
 check =0
        for i in range(len(A[0])):
            stack=[ord(x[i]) for x in A]
            if stack != sorted(stack):
                check += 1
            
        return check
	```
