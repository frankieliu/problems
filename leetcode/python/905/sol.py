
Python one line

https://leetcode.com/problems/sort-array-by-parity/discuss/237705

* Lang:    python3
* Author:  dacheng0413
* Votes:   2

```
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        return [i for i in A if i % 2 ==0]+[i for i in A if i % 2 != 0]
		```
