
O(k) python code

https://leetcode.com/problems/pascals-triangle-ii/discuss/38571

* Lang:    python3
* Author:  zsimath
* Votes:   4

class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in range(1,rowIndex+2):
            # there are i elements
            result.append(1)
            for j in range(i-2,0,-1):
                result[j] += result[j-1]
        return result
