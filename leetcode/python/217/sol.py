
One line solution in python

https://leetcode.com/problems/contains-duplicate/discuss/60850

* Lang:    python3
* Author:  lifeisshort
* Votes:   66

    class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
