
binary search for solving the issue of guess the picked number

https://leetcode.com/problems/guess-number-higher-or-lower/discuss/250594

* Lang:    python3
* Author:  DelandF
* Votes:   0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low,high=1,n
        mid=0
        while low<high:
            mid=low+(high-low)/2
            mid=int(mid)
            if guess(mid)==-1:
                high=mid-1
            elif guess(mid)==1:
                low=mid+1
            else:
                return mid
        return low
