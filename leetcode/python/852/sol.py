
Python one Line 20ms

https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/241390

* Lang:    python3
* Author:  dacheng0413
* Votes:   0

```
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
		```
